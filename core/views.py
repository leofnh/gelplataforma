from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento,Submissao,Formulario, Usuariocd, cpfteste, Sessoes,Inscritos, Avaliadores,Criterios
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum,Count



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
            return redirect('/home/')
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

    id = request.GET.get('id')

    sessao_id_evento = Sessoes.objects.filter(id=id)
    for s in sessao_id_evento:
        id_do_evento = s.id_evento
    #sessao = Sessoes.objects.filter(id_evento=id)
    eventos = Evento.objects.all()
    sessaoid = Sessoes.objects.filter(id=id)
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        id_usuario = m.id
    for s in sessaoid:
        id_evento = s.id_evento
    #verificar = Submissao.objects.filter(id=id, id_usuario=id_usuario)
    #if verificar:
     #   msg = 'Você já enviou um trabalho para esta sessão!'
     #   sessao = Sessoes.objects.filter(id=id)
     #   evento = Evento.objects.filter(id=id_do_evento)
     #   dados = {'id': id,
     #            'msg': msg,
     #            'evento': evento,
     #            'sessao': sessao}
     #   return render(request,'submeter.html', dados)
    #else:

    if request.POST['sessao'] == 'Selecione a sessão...':

        msg = 'Escolha uma sessão!'
        sessao = Sessoes.objects.filter(id=id)
        evento = Evento.objects.filter(id=id_do_evento)
        dados = {'id':id,
               'msg':msg,
               'evento':evento,
              'sessao':sessao}
        return render(request,'submeter.html', dados)
    else:

        if request.FILES.get('trabalho'):

            trabalhoenviar = request.FILES.get('trabalho')
            Submissao.objects.create(
                    trabalho = trabalhoenviar,
                    sessao = id,
                    id_evento = id_evento,
                    id_usuario = id_usuario,
                    status = 'avaliacao',
                    av1 = 'aguardando',
                    av2 = 'aguardando'
                )
            msg2 = 'Você enviou seu trabalho com sucesso!'
            sessao = Sessoes.objects.filter(id=id)
            evento = Evento.objects.filter(id=id_do_evento)
            dados = {'id':id,
                         'msg2':msg2,
                         'eventos':eventos,
                         'evento':evento,
                         'sessao':sessao}
            return render(request,'submeter.html', dados)
        else:

            msg = 'Selecione seu trabalho para enviar!'
            sessao = Sessoes.objects.filter(id=id)
            evento = Evento.objects.filter(id=id_do_evento)
            dados = {'id':id,
                         'msg':msg,
                         'eventos':eventos,
                         'evento':evento,
                          'sessao':sessao }
            return render(request,'submeter.html', dados)



def testecpf(request):

    cpf = request.POST['cpf']
    data = {}

    if len(cpf) > 11 or len(cpf) < 11:
        data['msg'] = 'CPF Inválido'
        return render(request,'novocadastro.html', data)
    else:
        lista_numero = []
        for i in cpf:
            lista_numero.append(int(i))

        if lista_numero[0] == lista_numero[1] and lista_numero[0] == lista_numero[2] and lista_numero[0] == lista_numero[3] and lista_numero[0] == lista_numero[4] and lista_numero[0] == lista_numero[5] and lista_numero[0] == lista_numero[6] and lista_numero[0] == lista_numero[7]:
            data['msg'] = 'CPF inválido'
            return render(request,'novocadastro.html', data)
        else:
            resultado = 0
            acumulador = 0
            controlador = 10

            for numeros in lista_numero[0:9]:
                resultado = numeros * controlador
                acumulador += resultado
                controlador = controlador -1
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
                    cpfteste.objects.create(
                        cpf = cpf
                    )
                    data['msg'] = 'CPF cadastrado com sucesso!'
                    return render(request,'novocadastro.html', data)

                else:

                    data['msg'] = 'CPF Inválido'
                    return render(request, 'novocadastro.html', data)

            else:
                data['msg'] = 'CPF Inválido'
                return render(request, 'novocadastro.html', data)


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
             'eventos': eventos}
    return render(request, 'alterarperfil.html', dados)


@login_required(login_url='/login/')
def attperfil(request):

    id = request.GET.get('id')
    usuario = User.objects.filter(username=request.user)
    data = {}
    for u in usuario:
        meuid = u.id

    vuser = Usuariocd.objects.filter(id_usuario=id, cpf=request.user)

    if vuser:

        if request.FILES.get('fotoperfil'):
            Submissao.objects.create(trabalho=request.FILES.get('fotoperfil'), id_evento=0)
            Usuariocd.objects.filter(id_usuario=meuid).update(perfil=request.FILES.get('fotoperfil'))
            return redirect('/home/')

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
    evento = Evento.objects.filter(id=id)
    sessao = Sessoes.objects.filter(id_evento=id)
    dados = {'evento':evento,
             'sessao':sessao}

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
    candidato = Usuariocd.objects.all()
    meuid = User.objects.filter(username=request.user)
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)

    # filter lider = sim
    evento = Evento.objects.filter(id=id)
    dados = {'id':id,
             'evento':evento,
             'candidato':candidato,
             'usuarios':usuarios}

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
            tema = request.POST['tema']
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
    eventos = Evento.objects.filter(id=id)
    sessao = Sessoes.objects.filter(id_evento=id)
    dados = {'id':id,
             'evento':eventos,
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
    for m in meuid:
        mid = m.id
    usuarios = Usuariocd.objects.filter(id_usuario=mid)
    dados = {'submetidos':submetidos,
             'usuarios':usuarios,
             'eventos':eventos,
             'sessao':sessao,
             'trabalho':trabalho}
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
    #acharav1 = Usuariocd.objects.filter(id_usuario=nome1)
    #acharav2 = Usuariocd.objects.filter(id_usuario=nome2)
    #acharav3 = Usuariocd.objects.filter(id_usuario=nome3)
    criterios = Criterios.objects.filter(id_sessao=id)
    total_criterios = Criterios.objects.filter(id_sessao=id).aggregate(total_sum=Count('id'))

    if request.POST['criterio']:

        criterio = request.POST['criterio']
        Criterios.objects.create(
            criterio = criterio,
            id_sessao = id,
        )
        msgc = 'Critério adicionado com sucesso!'
        dados = {'id': id,
                 'evento': evento,
                 'sessao': sessao,
                 'total_submetidos': total_submetidos,
                 'candidato': candidato,
                 'msgc': msgc,
                 'avaliadores': avaliadores,
              #   'acharav1': acharav1,
               #  'acharav2': acharav2,
                # 'acharav3': acharav3,
                 'criterios':criterios,
                 'total_criterios':total_criterios
                 }
        return render(request,'editarsessao.html', dados)
    else:
        msgc2 = 'Formule o critério para cria-lo'
        dados = {'id': id,
                 'evento': evento,
                 'sessao': sessao,
                 'total_submetidos': total_submetidos,
                 'candidato': candidato,
                 'msgc2': msgc2,
                 'avaliadores': avaliadores,
                 'acharav1': acharav1,
                 'acharav2': acharav2,
                 'acharav3': acharav3,
                 'criterios':criterios,
                 'total_criterios':total_criterios
                 }
        return render(request, 'editarsessao.html', dados)

@login_required(login_url='/login/')
def avaliartrabalho(request):
    id = request.GET.get('id')
    acharevento = Submissao.objects.filter(id=id)
    for a in acharevento:
        id_evento = a.id_evento
        id_sessao = a.sessao
    evento = Evento.objects.filter(id=id_evento)
    criterios = Criterios.objects.filter(id_sessao=id_sessao)
    sessao = Sessoes.objects.filter(id=id_sessao)
    submetidos = Submissao.objects.filter(id=id)
    dados = {'id':id,
             'evento':evento,
             'criterios':criterios,
             'sessao':sessao,
             'submetidos':submetidos}
    return render(request,'avaliartrabalho.html', dados)

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