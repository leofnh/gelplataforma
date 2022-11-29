import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from core.models import Evento,Submissao,Formulario, Usuariocd, Sessoes,Inscritos, Avaliadores,Criterios
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum,Count
from django.core.mail import send_mail


# Create your views here.
def logar(request):

    data = {}
    if request.method == "GET":
        data['msg'] = 'Algo deu errado, tente denovo!'
        return render(request,'login.html', data)
    else:

        usuario = request.POST['cpf']
        senha = request.POST['senha']
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request,user)
            return redirect('/principal/')
        else:
            data['msg'] = 'CPF ou SENHA inválido'
            return render(request,'login.html', data)


def novocadastrar(request):
    data = {}
    data['msg'] = 'Algo deu errado, por favor tente outra vez!'
    if request.method == "GET":
        return render(request,'novocadastro.html', data)
    else:

        if request.POST['cpf'] and request.POST['nome'] and request.POST['cep'] and request.POST['nascimento'] and request.POST['email'] and request.POST['endereco'] and request.POST['cidade'] and request.POST['bairro'] and request.POST['pais'] and request.POST['instituicao'] and request.POST['cmp'] and request.POST['categ'] and request.POST['cinfo'] and request.POST['senha'] and request.POST['senha2']:
            cpf = request.POST['cpf']
            nome = request.POST['nome']
            cep = request.POST['cep']
            nascimento = request.POST['nascimento']
            email = request.POST['email']
            endereco = request.POST['endereco']
            cidade = request.POST['cidade']
            bairro = request.POST['bairro']
            pais = request.POST['pais']
            instituicao = request.POST['instituicao']
            cmp = request.POST['cmp']
            categ = request.POST['categ']
            cinfo = request.POST['cinfo']
            senha = request.POST['senha']
            senha2 = request.POST['senha2']
            contato = request.POST['contato']

            if len(cpf) > 11 or len(cpf) < 11:
                data['msg'] = 'CPF Inválido'
                return render(request, 'novocadastro.html', data)
            else:
                lista_numero = []
                for i in cpf:
                    lista_numero.append(int(i))
                if lista_numero[0] == lista_numero[1] and lista_numero[0] == lista_numero[2] and lista_numero[0] == \
                        lista_numero[3] and lista_numero[0] == lista_numero[4] and lista_numero[0] == lista_numero[
                    5] and lista_numero[0] == lista_numero[6] and lista_numero[0] == lista_numero[7]:
                    data['msg'] = 'CPF inválido'
                    return render(request, 'novocadastro.html', data)
                else:
                    resultado = 0
                    acumulador = 0
                    controlador = 10

                    for numeros in lista_numero[0:9]:
                        resultado = numeros * controlador
                        acumulador += resultado
                        controlador = controlador - 1
                    acumulador = (acumulador * 10) % 11

                    if acumulador == 10:
                        acumulador = 0
                    if acumulador == lista_numero[9]:
                        resultado2 = 0
                        acumulador2 = 0
                        controlador2 = 11
                        for numeros2 in lista_numero[0:10]:
                            resultado2 = numeros2 * controlador2
                            acumulador2 += resultado2
                            controlador2 = controlador2 - 1

                        acumulador2 = (acumulador2 * 10) % 11

                        if acumulador2 == 10:
                            acumulador2 = 0
                        if acumulador2 == lista_numero[10]:

                            verificauser = User.objects.filter(username=cpf)
                            if verificauser:
                                data['msg'] = 'Este CPF já foi cadastrado em nosso sistema!'
                                return render(request, 'novocadastro.html', data)
                            else:

                                if senha == senha2:

                                    criaruser = User.objects.create_user(username=cpf, email=email,
                                                                         password=senha, first_name=nome
                                                                         )
                                    criaruser.save()
                                    acharid = User.objects.filter(username=cpf)
                                    if acharid:
                                        for i in acharid:
                                            id = i.id

                                        Usuariocd.objects.create(
                                            cpf=cpf,
                                            nome=nome,
                                            cep=cep,
                                            nascimento=nascimento,
                                            email=email,
                                            endereco=endereco,
                                            cidade=cidade,
                                            bairro=bairro,
                                            pais=pais,
                                            instituicao=instituicao,
                                            cmp=cmp,
                                            categ=categ,
                                            cinfo=cinfo,
                                            gestor_plataforma='nao',
                                            autor='nao',
                                            avaliador='nao',
                                            contato=contato,
                                            perfil='avatarp.png',
                                            id_usuario=id
                                        )

                                        data['cadastrou'] = 'Bem vindo {} você foi cadastrado com sucesso!'.format(nome)
                                        return render(request, 'novocadastro.html', data)

                                    else:
                                        data['msg'] = 'Algo deu errado, tente outra vez!'
                                        return render(request, 'novocadastro.html', data)



                                else:
                                    data['msg'] = 'Você digitou duas senhas diferente!'
                                    return render(request, 'novocadastro.html', data)

                        else:

                            data['msg'] = 'CPF Inválido'
                            return render(request, 'novocadastro.html', data)

                    else:
                        data['msg'] = 'CPF Inválido'
                        return render(request, 'novocadastro.html', data)

        else:
            data['msg'] = 'Preencha todos os campos do formulário!'
            return render(request, 'novocadastro.html', data)


def teste(request):

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    dados = {'eventos':eventos,
             'usuarios':usuarios}

    return render(request,'layout-static.html', dados)

def logando(request):

    return render(request,'login.html')

def novocadastro(request):

    return render(request, 'novocadastro.html')

@login_required(login_url='/login/')
def home(request):
    id = request.GET.get('id')
    if id is None: return redirect('/home/?id=home')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.all()
    total_eventos = Evento.objects.all().aggregate(sum_total=Count('id'))
    total_eventos_andamento = Evento.objects.filter(status='andamento').aggregate(sum_total=Count('id'))
    total_eventos_finalizado = Evento.objects.filter(status='finalizado').aggregate(sum_total=Count('id'))
    total_submissao = Submissao.objects.filter(status='avaliacao').aggregate(sum_total=Count('id'))
    tainscrito = Inscritos.objects.filter(cpf=mid)
    evento_inscrito = Evento.objects.filter(status='andamento')

    dados = {'usuarios':usuarios,
             'id':id,
             'eventos':eventos,
             'total_eventos':total_eventos,
             'total_eventos_andamento':total_eventos_andamento,
             'total_eventos_finalizado':total_eventos_finalizado,
             'evento_inscrito':evento_inscrito,
             'tainscrito':tainscrito,
             'total_submissao':total_submissao
             }
    return render(request, 'inicial.html', dados)

def criarevento(request):

    id = request.GET.get('id')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    if request.POST['nomeevento'] and request.POST['cidadeevento'] and request.POST['inicioevento'] and request.POST['modalidadeevento'] and request.POST['estadoevento']:
        if request.FILES.get('logoevento'):
            logoevento = request.FILES.get('logoevento')
        else:
            logoevento = 'logoeventopadrao'

        Evento.objects.create(
            nome = request.POST['nomeevento'],
            cidade = request.POST['cidadeevento'],
            data_evento = request.POST['inicioevento'],
            modalidade = request.POST['modalidadeevento'],
            logo = logoevento,
            estado = request.POST['estadoevento'],
            status = 'andamento'
        )

        nomeevento = request.POST['nomeevento']
        cidadeevento = request.POST['cidadeevento']
        dataevento = request.POST['inicioevento']
        modaevento = request.POST['modalidadeevento']
        estado = request.POST['estadoevento']
        #idevento = Evento.objects.filter(nome=nomeevento,cidade=cidadeevento,data_evento=dataevento)
        #for i in idevento:
        #    ide = i.id

        msg = 'Você criou o evento {} para {} na modalidade {} em {} - {}'.format(nomeevento, dataevento, modaevento, cidadeevento, estado)
        dados = {'msg':msg,
                 'id':id,
                 'usuarios':usuarios}
        return render(request,'criarevento.html', dados)


    else:
        msg = 'Preencha todos os campos corretamente para efetuar o cadastro!'
        dados = {'msg':msg,
                 'id':id,
                 'usuarios':usuarios}
        return render(request,'criarevento.html', dados)

def submetertrabalho(request):

    if request.POST['sessao'] == 'Selecione a sessão...':
        msg = 'Escolha uma sessão!'
        sessao = Sessoes.objects.all()
        evento = Evento.objects.all()
        meuid = User.objects.filter(username=request.user)
        for m in meuid:
            mid = m.id
        usuarios = Usuariocd.objects.filter(id_usuario=mid)

        dados = {'id':id,
               'msg':msg,
               'evento':evento,
              'sessao':sessao,
              'usuarios':usuarios}
        return render(request,'submeter.html', dados)
    else:

        meuid = User.objects.filter(username=request.user)
        for m in meuid:
            mid = m.id
        meunome = Usuariocd.objects.filter(id_usuario=mid)
        for meu in meunome:
            nome = meu.nome
            email = meu.email
        id_da_sessao = request.POST['sessao']
        acharevento = Sessoes.objects.filter(id=id_da_sessao)
        meuid = User.objects.filter(username=request.user)
        for m in meuid:
            mid = m.id
        usuarios = Usuariocd.objects.filter(id_usuario=mid)
        for i in acharevento:
            id_evento = i.id_evento
        eventos = Evento.objects.all()
        if request.FILES.get('trabalho'):
            trabalhoenviar = request.FILES.get('trabalho')
            chave = request.POST['palavrachave']
            resumo = request.POST['resumo']
            titulo = request.POST['titulo']
            autor1 = request.POST['autor1']

            Submissao.objects.create(
                    trabalho = trabalhoenviar,
                    sessao = id_da_sessao,
                    id_evento = id_evento,
                    id_usuario = mid,
                    status = 'avaliacao',
                    av1 = 'aguardando',
                    av2 = 'aguardando',
                    titulo=titulo,
                    chave=chave,
                    resumo=resumo,
                    autor=autor1,
                    progresso=0
                )

            mensagem = 'Olá, {} você acabou de submeter um trabalho, aguarde até que ele seja avaliado, você será avisado por e-mail. Titulo do trabalho {}, autor {}'.format(nome, titulo, autor1)

            send_mail('G&L Plataforma de Eventos', mensagem, 'gelplataforma@gmail.com',
                      recipient_list=[email,'alex@gilbertodamata.com.br', 'leofnh@live.com', 'leonardobastos4@gmail.com'])
            #return HttpResponse('e-mail enviado')
            msg2 = 'Você enviou seu trabalho com sucesso!'
            sessao = Sessoes.objects.filter(id_evento=id_evento)
            evento = Evento.objects.filter(id=id_evento)
            dados = {'id':id,
                         'msg2':msg2,
                         'eventos':eventos,
                         'evento':evento,
                         'sessao':sessao,
                     'usuarios':usuarios}
            return render(request,'submeter.html', dados)
        else:
            msg = 'Selecione seu trabalho para enviar!'
            sessao = Sessoes.objects.filter(id_evento=id_evento)
            evento = Evento.objects.filter(id=id_evento)
            dados = {'id':id,
                         'msg':msg,
                         'eventos':eventos,
                         'evento':evento,
                          'sessao':sessao,
                     'usuarios':usuarios}
            return render(request,'submeter.html', dados)





@login_required(login_url='/login/')
def meuperfil(request):

    id = request.GET.get('id')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.all()

    dados = {'usuarios': usuarios,
             'id': id,
             'eventos': eventos,
             'mid':mid}
    return render(request, 'alterarperfil.html', dados)


@login_required(login_url='/login/')
def attperfil(request):
    id = request.GET.get('id')
    usuario = User.objects.filter(username=request.user)
    data = {}
    for u in usuario:
        meuid = u.id

    vuser = Usuariocd.objects.filter(id_usuario=meuid, cpf=request.user)

    if vuser:
        Usuariocd.objects.filter(id_usuario=meuid).update(
            nome = request.POST['nome'],
            email = request.POST['email'],
            contato = request.POST['contato'],
            endereco = request.POST['endereco'],
            instituicao = request.POST['instituicao']
        )

        if request.FILES.get('fotoperfil'):
            #Submissao.objects.create(trabalho=request.FILES.get('fotoperfil'), id_evento=0)
            Usuariocd.objects.filter(id_usuario=meuid).update(perfil=request.FILES.get('fotoperfil'))
            return redirect('/meuperfil/')

        else:
            return redirect('/meuperfil/')

    else:
        data['msg'] = 'Você não tem autorização para executar este comando!'
        return render(request,'inicial.html', data)

def gerenciarevento(request):
    id = request.GET.get('id')

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    total_eventos = Evento.objects.all().aggregate(sum_total=Count('id'))
    total_eventos_andamento = Evento.objects.filter(status='andamento').aggregate(sum_total=Count('id'))
    total_eventos_finalizado = Evento.objects.filter(status='finalizado').aggregate(sum_total=Count('id'))

    dados = {'usuarios': usuarios,
             'id': id,
             'eventos': eventos,
             'total_eventos': total_eventos,
             'total_eventos_andamento': total_eventos_andamento,
             'total_eventos_finalizado': total_eventos_finalizado,
             }

    return render(request,'gerenciarevento.html', dados)

@login_required(login_url='/login/')
def editarevento(request):

    id = request.GET.get('id')

    # verificar se é gestor
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    formulario = Formulario.objects.filter(id_evento=id)
    evento = Evento.objects.filter(id=id)
    sessao = Sessoes.objects.filter(id_evento=id)
    contar_formulario = Formulario.objects.filter(id_evento=id).aggregate(sum_total=Count('id'))
    candidato = Usuariocd.objects.all()
    dados = {'evento':evento,
             'sessao':sessao,
             'eventos': eventos,
             'usuarios': usuarios,
             'id':id,
             'formulario':formulario,
             'contar_formulario':contar_formulario,
             'candidato':candidato
             }

    return render(request, 'editarevento.html', dados)

@login_required(login_url='/login/')
def alterarevento(request):
    id = request.GET.get('id')
    # verificar se é gestor
    valteracao = Evento.objects.filter(id=id)
    evento = Evento.objects.filter(id=id)
    for v in valteracao:
        nome = v.nome
        cidade = v.cidade
        estado = v.estado
        modalidade = v.modalidade
        data = v.data_evento
    # verificando se há alteração no evento

    if request.POST['nome'] != nome or request.POST['cidade'] != cidade or request.POST['estado'] != estado or request.POST['datahora'] or request.POST['modalidade'] != modalidade:


        if request.POST['nome'] != nome:
            Evento.objects.filter(id=id).update(nome=request.POST['nome'])
        if request.POST['cidade'] !=cidade:
            Evento.objects.filter(id=id).update(cidade=request.POST['cidade'])
        if request.POST['estado'] != estado:
            Evento.objects.filter(id=id).update(estado=request.POST['estado'])
        if request.POST['datahora'] and request.POST['datahora'] != data:
            Evento.objects.filter(id=id).update(data_evento=request.POST['datahora'])
        if request.POST['modalidade'] != modalidade:
            Evento.objects.filter(id=id).update(modalidade=request.POST['modalidade'])

        msg = 'Evento editado com sucesso!'
        dados = {'id':id,
                 'msg':msg,
                 'evento':evento}
        return render(request, 'editarevento.html', dados)
    else:

        return redirect('/editarevento/?id={}'.format(id))



@login_required(login_url='/login/')
def addsessao(request):

    id = request.GET.get('id')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    formulario = Formulario.objects.filter(id_evento=id)
    contar_formulario = Formulario.objects.filter(id_evento=id).aggregate(sum_total=Count('id'))
    candidato = Usuariocd.objects.all()

    # filter lider = sim
    evento = Evento.objects.filter(id=id)
    dados = {'id':id,
             'evento':evento,
             'candidato':candidato,
             'usuarios':usuarios,
             'formulario':formulario,
             'contar_formulario':contar_formulario}

    return render(request,'addsessao.html', dados)


@login_required(login_url='/login/')
def criarsessao(request):
    id = request.GET.get('id')
    evento = Evento.objects.filter(id=id)
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)

    if request.POST['lider'] != 'Selecione o Líder...':
        Sessoes.objects.create(
            nome=request.POST['nome'],
            descricao=request.POST['descricao'],
            id_evento = id,
            lider = request.POST['lider'],
            tema = request.POST['tema'],
            formulario = request.POST['formulario']
        )
        msg = 'Você criou uma sessão com sucesso!'
        dados  = {'id':id,
                  'evento':evento,
                  'msg':msg,
                  'usuarios':usuarios}

        return render(request,'addsessao.html', dados)

    else:
        msg2 = 'Escolha um líder!'
        dados = {'id': id,
                 'evento': evento,
                 'msg2': msg2,
                 'usuarios':usuarios}

        return render(request, 'addsessao.html', dados)

@login_required(login_url='/login/')
def inscrever(request):

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    eventos = Evento.objects.filter(status='andamento')
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    dados = {'eventos':eventos,
             'usuarios':usuarios}


    return render(request,'inscricao.html', dados)


@login_required(login_url='/login/')
def inscricao(request):

    id = request.GET.get('id')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    meunome = Usuariocd.objects.filter(id_usuario=mid)
    for mn in meunome:
        nome = mn.nome
    eventos = Evento.objects.filter(status='andamento')
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    vevento = Inscritos.objects.filter(id_evento=id, cpf=mid)
    if vevento:
        msg = 'Você já esta cadastrado neste evento!'
        dados = {'id':id,
                 'eventos':eventos,
                 'usuarios':usuarios,
                 'msg':msg}
        return render(request,'inscricao.html', dados)
    else:

        msg2 = 'Você se cadastrou para o evento!'

        Inscritos.objects.create(
            id_evento=id,
            cpf=mid,
            nome=nome
        )

        dados = {'id': id,
                 'eventos': eventos,
                 'usuarios': usuarios,
                 'msg2': msg2}

        return render(request,'inscricao.html', dados)

@login_required(login_url='/login/')
def submeter(request):

    id = request.GET.get('id')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    #eventos = Evento.objects.filter(id=id)
    #sessao = Sessoes.objects.filter(id_evento=id)
    eventos = Evento.objects.filter(status='andamento')
    sessao = Sessoes.objects.all()
    dados = {'id':id,
             'eventos':eventos,
             'sessao':sessao,
             'usuarios':usuarios}
    return render(request,'submeter.html', dados)

@login_required(login_url='/login/')
def submetidos(request):

    submetidos = Submissao.objects.filter(status='avaliacao')
    meuid = User.objects.filter(username=request.user)
    eventos = Evento.objects.all()
    sessao = Sessoes.objects.all()
    trabalho = Submissao.objects.all()
    avaliadores = Usuariocd.objects.all()
    teste = Submissao.objects.all()


    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    dados = {'submetidos':submetidos,
             'usuarios':usuarios,
             'eventos':eventos,
             'sessao':sessao,
             'trabalho':trabalho,
             'avaliadores':avaliadores,
             'teste':teste}
    return render(request,'submetidos.html', dados)

@login_required(login_url='/login/')
def editarsessao(request):

    id = request.GET.get('id')
    acharevento = Sessoes.objects.filter(id=id)
    for a in acharevento:
        id_evento = a.id_evento
    evento = Evento.objects.filter(id=id_evento)
    sessao = Sessoes.objects.filter(id=id)
    total_submetidos = Submissao.objects.filter(sessao=id).aggregate(sum_total=Count('id'))
    candidato = Usuariocd.objects.all()
    avaliadores = Avaliadores.objects.filter(id_sessao=id)
    for av in avaliadores:
        nome1 = av.av1
        nome2 = av.av2
        nome3 = av.av3

    criterios = Criterios.objects.filter(id_sessao=id)
    total_criterios = Criterios.objects.filter(id_sessao=id).aggregate(total_sum=Count('id'))

    dados = {'id':id,
            'evento':evento,
            'sessao':sessao,
            'total_submetidos':total_submetidos,
            'candidato':candidato,
            'avaliadores':avaliadores,
            'criterios':criterios,
            'total_criterios':total_criterios
             }

    return render(request,'editarsessao.html', dados)


@login_required(login_url='/login/')
def addavaliadores(request):

    id = request.GET.get('id')
    acharevento = Sessoes.objects.filter(id=id)
    for a in acharevento:
        id_evento = a.id_evento
    evento = Evento.objects.filter(id=id_evento)
    sessao = Sessoes.objects.filter(id=id)
    total_submetidos = Submissao.objects.filter(sessao=id).aggregate(sum_total=Count('id'))
    candidato = Usuariocd.objects.all()
    avaliadores = Avaliadores.objects.filter(id_sessao=id)
    for av in avaliadores:
        nome1 = av.av1
        nome2 = av.av2
        nome3 = av.av3

    acharav1 = Usuariocd.objects.filter(id_usuario=nome1)
    acharav2 = Usuariocd.objects.filter(id_usuario=nome2)
    acharav3 = Usuariocd.objects.filter(id_usuario=nome3)
    criterios = Criterios.objects.filter(id_sessao=id)
    total_criterios = Criterios.objects.filter(id_sessao=id).aggregate(total_sum=Count('id'))
    if request.POST['av1'] != 'Escolha o Avaliador 1' and request.POST['av2'] != 'Escolha o Avaliador 2' and request.POST['av3'] != 'Escolha o Avaliador 3':

        if request.POST['av1'] != request.POST['av2'] and request.POST['av1'] != request.POST['av3']:

            if request.POST['av2'] != request.POST['av3']:

                av1 = request.POST['av1']
                av2 = request.POST['av2']
                av3 = request.POST['av3']

                Avaliadores.objects.create(
                    av1 = av1,
                    av2 = av2,
                    av3 = av3,
                    id_sessao = id
                )
                msg2 = 'Avaliadores adicionados com sucesso!'
                if acharv1 and acharv2 and acharv3:
                    dados = {'id': id,
                             'evento': evento,
                             'sessao': sessao,
                             'total_submetidos': total_submetidos,
                             'candidato': candidato,
                             'msg2':msg2,
                             'avaliadores': avaliadores,
                             'acharav1': acharav1,
                             'acharav2': acharav2,
                             'acharav3': acharav3,
                             'criterios': criterios,
                             'total_criterios':total_criterios
                             }
                    return render(request,'editarsessao.html', dados)
                else:
                    dados = {'id': id,
                             'evento': evento,
                             'sessao': sessao,
                             'total_submetidos': total_submetidos,
                             'candidato': candidato,
                             'msg2': msg2,
                             'avaliadores': avaliadores,
                             'criterios': criterios,
                             'total_criterios': total_criterios
                             }
                    return render(request, 'editarsessao.html', dados)

            else:
                msg = 'Não é permitido escolher avaliadores repetidos!'
                dados = {'id': id,
                         'evento': evento,
                         'sessao': sessao,
                         'total_submetidos': total_submetidos,
                         'candidato': candidato,
                         'msg': msg,
                         'avaliadores': avaliadores,
                         'acharav1': acharav1,
                         'acharav2': acharav2,
                         'acharav3': acharav3,
                         'criterios': criterios,
                         'total_criterios':total_criterios
                         }
                return render(request, 'editarsessao.html', dados)

        else:
            msg = 'Não é permitido escolher avaliadores repetidos!'
            dados = {'id': id,
                     'evento': evento,
                     'sessao': sessao,
                     'total_submetidos': total_submetidos,
                     'candidato': candidato,
                     'msg': msg,
                     'avaliadores': avaliadores,
                     'acharav1': acharav1,
                     'acharav2': acharav2,
                     'acharav3': acharav3,
                     'criterios': criterios,
                     'total_criterios':total_criterios
                     }
            return render(request, 'editarsessao.html', dados)

    else:
        msg = 'Escolha os avaliadores!'
        dados = {'id': id,
                 'evento': evento,
                 'sessao': sessao,
                 'total_submetidos': total_submetidos,
                 'candidato': candidato,
                 'msg': msg,
                 'avaliadores': avaliadores,
                 'acharav1': acharav1,
                 'acharav2': acharav2,
                 'acharav3': acharav3,
                 'criterios': criterios,
                 'total_criterios':total_criterios
                 }
        return render(request, 'editarsessao.html', dados)

@login_required(login_url='/login/')
def addcriterio(request):
    id = request.GET.get('id')
    if request.POST['nomeformulario'] and request.POST['criterio'] and request.POST['criterio1'] and request.POST['criterio2'] and request.POST['criterio3'] and request.POST['criterio4'] and request.POST['criterio5'] and request.POST['criterio6'] and request.POST['criterio7'] and request.POST['criterio8'] and request.POST['criterio9']:
        c1 = request.POST['criterio']
        c2 = request.POST['criterio1']
        c3 = request.POST['criterio2']
        c4 = request.POST['criterio3']
        c5 = request.POST['criterio4']
        c6 = request.POST['criterio5']
        c7 = request.POST['criterio6']
        c8 = request.POST['criterio7']
        c9 = request.POST['criterio8']
        c10 = request.POST['criterio9']
        nome_formulario = request.POST['nomeformulario']
        Formulario.objects.create(

            nome_formulario=nome_formulario,
            c1=c1,
            c2=c2,
            c3=c3,
            c4=c4,
            c5=c5,
            c6=c6,
            c7=c7,
            c8=c8,
            c9=c9,
            c10=c10,
            id_evento = id
        )
        return redirect('/editarevento/?id={}'.format(id))
    else:
        msg = 'Aconteceu algum erro e não cadastrou seu formulário!'
        dados = {'id':id,
                 'msg':msg}
        return render(request,'editarevento.html', dados)



@login_required(login_url='/login/')
def avaliartrabalho(request):

    #id = request.GET.get('id')
    #acharevento = Submissao.objects.filter(id=id)
    #for a in acharevento:
    #    id_evento = a.id_evento
    #    id_sessao = a.sessao
    #evento = Evento.objects.filter(id=id_evento)
    #criterios = Criterios.objects.filter(id_sessao=id_sessao)
    #sessao = Sessoes.objects.filter(id=id_sessao)
    #submetidos = Submissao.objects.filter(id=id)
    #dados = {'id':id,
    #         'evento':evento,
    #         'criterios':criterios,
    #         'sessao':sessao,
    #         'submetidos':submetidos}

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id

    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    sessao = Sessoes.objects.all()
    formulario = Formulario.objects.all()

    avaliacao = Submissao.objects.filter(av1=mid)
    avaliacao2 = Submissao.objects.filter(av2=mid)
    avaliacao3 = Submissao.objects.filter(av3=mid)

    dados = {'eventos': eventos,
             'usuarios': usuarios,
             'sessao': sessao,
             'formulario': formulario,
             'avaliacao':avaliacao,
             'avaliacao2':avaliacao2,
             'avaliacao3':avaliacao3}
    return render(request,'avaliartrabalho.html',dados)

@login_required(login_url='/login/')
def enviaravaliacao(request):

    id = request.GET.get('id')
    trabalho_submetido = Submissao.objects.filter(id=id)
    for t in trabalho_submetido:
        sessao = t.sessao
    contar_criterios = Criterios.objects.filter(id_sessao=sessao).aggregate(total_sum=Count('id'))
    nota_total = 0
    forcriterios = Criterios.objects.filter(id_sessao=sessao)
    for c in forcriterios:
        nota = request.POST['av{}'.format(c.id)]
        nota_total += int(nota)
    maximo = contar_criterios['total_sum'] * 10
    minimo = maximo / 2
    vtrabalho = Submissao.objects.filter(id=id)
    for v in vtrabalho:
        av1 = v.av1
        av2 = v.av2
        av3 = v.av3
    if av1 == 'aguardando':
        if nota_total >= minimo:
            Submissao.objects.filter(id=id).update(
                av1 = 'aprovado'
            )
        else:
            Submissao.objects.filter(id=id).update(
                av1='reprovado'

            )
    else:
        if av2 == 'aguardando':
            if nota_total >= minimo:
                Submissao.objects.filter(id=id).update(
                    av2='aprovado',
                    status='avaliado'
                )
            else:
                Submissao.objects.filter(id=id).update(
                    av2='reprovado',
                    status='avaliado'
                )


    return redirect('/home/')

@login_required(login_url='/login/')
def avaliados(request):
    trabalhos = Submissao.objects.filter(status='avaliado')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    geral = Usuariocd.objects.all()
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.all()

    dados = {'trabalhos':trabalhos,
             'usuarios':usuarios,
             'eventos':eventos,
             'geral':geral}

    return render(request,'avaliados.html', dados)
@login_required(login_url='/login/')
def principal(request):

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    dados = {'eventos': eventos,
             'usuarios': usuarios}

    return render(request,'principal.html', dados)


@login_required(login_url='/login/')
def submissoes(request):

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    sessao = Sessoes.objects.all()
    dados = {'eventos': eventos,
             'usuarios': usuarios,
             'sessao':sessao}

    return render(request, 'submissoes.html', dados)
@login_required(login_url='/login/')
def criandoevento(request):

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    sessao = Sessoes.objects.all()
    dados = {'eventos': eventos,
             'usuarios': usuarios,
             'sessao': sessao}

    return render(request,'criarevento.html', dados)

@login_required(login_url='/login/')
def semlink(request):

    return redirect('/principal/')

@login_required(login_url='/login/')
def formulario(request):
    id = request.GET.get('id')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    sessao = Sessoes.objects.all()
    formulario = Formulario.objects.all()
    dados = {'eventos': eventos,
             'usuarios': usuarios,
             'sessao': sessao,
             'formulario':formulario}

    return render(request, 'formularios.html', dados)

@login_required(login_url='/login/')
def enviaravaliador(request):

    id = request.POST['id_trabalho']

    if request.POST['av3']:
        av3 = request.POST['av3']
        Submissao.objects.filter(id=id).update(
            av3=av3
        )
        return redirect('/submetidos/')
    else:

        if request.POST['av1'] or request.POST['av2']:
            if request.POST['av1']:
                av1 = request.POST['av1']
                Submissao.objects.filter(id=id).update(
                    av1=av1
                )

            if request.POST['av2']:
                av2 = request.POST['av2']
                Submissao.objects.filter(id=id).update(
                    av2=av2
                )
            return redirect('/submetidos/')

        else:
            msg = 'Houve algum erro, por favor selecione o avaliador!'
            submetidos = Submissao.objects.filter(status='avaliacao')
            meuid = User.objects.filter(username=request.user)
            eventos = Evento.objects.all()
            sessao = Sessoes.objects.all()
            trabalho = Submissao.objects.all()
            avaliadores = Usuariocd.objects.all()
            for m in meuid:
                mid = m.id

            usuarios = Usuariocd.objects.filter(id_usuario=mid)
            dados = {'submetidos': submetidos,
                     'usuarios': usuarios,
                     'eventos': eventos,
                     'sessao': sessao,
                     'trabalho': trabalho,
                     'avaliadores': avaliadores,
                     'msg':msg}

            return render(request, 'submetidos.html', dados)

@login_required(login_url='/login/')
def pontuartrabalho(request):

    id = request.GET.get('id')
    acharsessao = Submissao.objects.filter(id=id)
    for a in acharsessao:
        sessaoid = a.sessao
    acharformulario = Sessoes.objects.filter(id=sessaoid)
    for af in acharformulario:
        id_formulario = af.formulario
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id


    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    eventos = Evento.objects.filter(status='andamento')
    sessao = Sessoes.objects.all()
    formulario = Formulario.objects.filter(id=id_formulario)
    trabalho = Submissao.objects.filter(id=id)
    dados = {'eventos': eventos,
             'usuarios': usuarios,
             'sessao': sessao,
             'formulario': formulario,
             'id':id,
             'trabalho':trabalho}

    return render(request,'pontuartrabalho.html', dados)


@login_required(login_url='/login/')
def avaliarformulario(request):
    id = request.GET.get('id')
    hoje = datetime.datetime.now()
    if request.POST['av1'] != 'n' and request.POST['av2'] != 'n' and request.POST['av3'] != 'n'and request.POST['av4'] != 'n' and request.POST['av5'] != 'n' and request.POST['av6'] != 'n' and request.POST['av7'] != 'n'and request.POST['av8'] != 'n'and request.POST['av9'] != 'n'and request.POST['av10'] != 'n':
        meuid = User.objects.filter(username=request.user)
        av1 = int(request.POST['av1'])
        av2 = int(request.POST['av2'])
        av3 = int(request.POST['av3'])
        av4 = int(request.POST['av4'])
        av5 = int(request.POST['av5'])
        av6 = int(request.POST['av6'])
        av7 = int(request.POST['av7'])
        av8 = int(request.POST['av8'])
        av9 = int(request.POST['av9'])
        av10 = int(request.POST['av10'])
        for m in meuid:
            mid = m.id
        vtrabalho1 = Submissao.objects.filter(id=id, av1=mid)
        vtrabalho2 = Submissao.objects.filter(id=id, av2=mid)
        vtrabalho3 = Submissao.objects.filter(id=id, av3=mid)
        progressop = Submissao.objects.filter(id=id)
        for p in progressop:
            pr = int(p.progresso)
        progresso = pr + 33
        if vtrabalho1:
            nota = av1 + av2 + av3 + av4 + av5 + av6 + av7 + av8 + av9 + av10
            resultado = nota / 10
            if resultado >= 3:
                vstatusaprovado = Submissao.objects.filter(id=id, av2='aprovado')
                Submissao.objects.filter(id=id).update(

                    av1='aprovado',
                    data_av1=hoje,
                    nota1=resultado,
                    progresso= progresso,
                    a1=mid
                )
                if vstatusaprovado:
                    Submissao.objects.filter(id=id).update(
                        status='aprovado',
                        progresso=100
                    )
                return redirect('/avaliartrabalho/')
            else:
                reprovou = Submissao.objects.filter(id=id, av2='reprovado')
                Submissao.objects.filter(id=id).update(
                    av1='reprovado',
                    data_av1=hoje,
                    nota1=resultado,
                    progresso= progresso,
                    a1=mid
                )
                if reprovou:
                    Submissao.objects.filter(id=id, status='reprovado', progresso=100)
                return redirect('/avaliartrabalho/')
        if vtrabalho2:

            nota = av1 + av2 + av3 + av4 + av5 + av6 + av7 + av8 + av9 + av10
            resultado = nota / 10

            if resultado >= 3:
                Submissao.objects.filter(id=id).update(
                    av2='aprovado',
                    data_av2=hoje,
                    nota2=resultado,
                    progresso= progresso,
                    a2 = mid
                )
                vstatusaprovado = Submissao.objects.filter(id=id, av1='aprovado')
                if vstatusaprovado:
                    Submissao.objects.filter(id=id).update(
                        status='aprovado',
                        progresso=100
                    )
                return redirect('/avaliartrabalho/')
            else:
                reprovou = Submissao.objects.filter(id=id, av1='reprovado')
                Submissao.objects.filter(id=id).update(
                    av2='reprovado',
                    data_av2=hoje,
                    nota2=resultado,
                    progresso= progresso,
                    a2 = mid
                )
                if reprovou:
                    Submissao.objects.filter(id=id).update(
                        status='reprovado',
                        progresso=100
                    )
                return redirect('/avaliartrabalho/')
        if vtrabalho3:
            nota = av1 + av2 + av3 + av4 + av5 + av6 + av7 + av8 + av9 + av10
            resultado = nota / 10

            if resultado >= 3:
                Submissao.objects.filter(id=id).update(
                    av3='aprovado',
                    data_av3=hoje,
                    nota3=resultado,
                    status='aprovado',
                    progresso=100,
                    a3=mid
                )

                return redirect('/avaliartrabalho/')
            else:

                Submissao.objects.filter(id=id).update(
                    av3='reprovado',
                    data_av2=hoje,
                    nota2=resultado,
                    status='reprovado',
                    progresso=100,
                    a3=mid
                )
                return redirect('/avaliartrabalho/')


    else:
        msg = 'Preencha as notas corretamente!'
        acharsessao = Submissao.objects.filter(id=id)
        for a in acharsessao:
            sessaoid = a.sessao
        acharformulario = Sessoes.objects.filter(id=sessaoid)
        for af in acharformulario:
            id_formulario = af.formulario
        meuid = User.objects.filter(username=request.user)
        for m in meuid:
            mid = m.id
        usuarios = Usuariocd.objects.filter(id_usuario=mid)
        eventos = Evento.objects.filter(status='andamento')
        sessao = Sessoes.objects.all()
        formulario = Formulario.objects.filter(id=id_formulario)
        trabalho = Submissao.objects.filter(id=id)
        dados = {'eventos': eventos,
                 'usuarios': usuarios,
                 'sessao': sessao,
                 'formulario': formulario,
                 'id': id,
                 'trabalho': trabalho,
                 'msg':msg}
        return render(request,'pontuartrabalho.html', dados)

@login_required(login_url='/login/')
def editarformulario(request):
    id = request.GET.get('id')
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    formulario = Formulario.objects.filter(id=id)


    dados = {'usuarios': usuarios,
             'id': id,
             'formulario':formulario
             }
    return render(request, 'editarformulario.html', dados)

@login_required(login_url='/login/')
def salvarformulario(request):
    id = request.GET.get('id')

    Formulario.objects.filter(id=id).update(
        c1=request.POST['c1'],
        c2=request.POST['c2'],
        c3=request.POST['c3'],
        c4=request.POST['c4'],
        c5=request.POST['c5'],
        c6=request.POST['c6'],
        c7=request.POST['c7'],
        c8=request.POST['c8'],
        c9=request.POST['c9'],
        c10=request.POST['c10'],
        nome_formulario=request.POST['nome']

    )

    return redirect('/editarformulario/?id={}'.format(id))

@login_required(login_url='/login/')
def arquivos(request):

    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    avaliados = Submissao.objects.filter(a1=mid)
    avaliados2 = Submissao.objects.filter(a2=mid)
    avaliados3 = Submissao.objects.filter(a3=mid)
    sessao = Sessoes.objects.all()
    arquivos = avaliados and avaliados2 and avaliados3

    dados = {'usuarios': usuarios,
              'arquivos':arquivos,
             'sessao':sessao
                     }
    return render(request, 'arquivos.html', dados)

@login_required(login_url='/login/')
def deslogar(request):

    logout(request)
    return redirect('/login/')

def verjs(request):
    return render(request,'add.html')

def eviaremail(request):

    try:
        mensagem = 'Email enviado com sucesso! Agora é só configurar cada envio.'
        send_mail('G&L Plataforma de Eventos', mensagem, 'gelplataforma@gmail.com',
                  recipient_list=['alex@gilbertodamata.com.br', 'leofnh@live.com', 'leonardobastos4@gmail.com'])
        return HttpResponse('e-mail enviado')
    except:

        return HttpResponse('e-mail não enviado')