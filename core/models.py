from django.db import models
from cpf_field.models import CPFField


# Create your models here.
class Evento(models.Model):

    nome = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=5)
    data_evento = models.DateTimeField()
    #dia1 = models.DateTimeField()
    #dia2 = models.DateTimeField()
    #dia3 = models.DateTimeField()
    modalidade = models.CharField(max_length=150)
    status = models.CharField(max_length=30)
    data_criacao = models.DateTimeField(auto_now=True)
    logo = models.FileField(upload_to='')


    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y às %H:%M')
    #def get_dia1(self):
    #    return self.dia1.strftime('%d/%m/%Y às %H:%M')
    #def get_dia2(self):
    #    return self.dia2.strftime('%d/%m/%Y às %H:%M')
    #def get_dia3(self):
    #    return self.dia3.strftime('%d/%m/%Y às %H:%M')


class Formulario(models.Model):

    c1 = models.CharField(max_length=500)
    c2 = models.CharField(max_length=500)
    c3 = models.CharField(max_length=500)
    c4 = models.CharField(max_length=500)
    c5 = models.CharField(max_length=500)
    c6 = models.CharField(max_length=500)
    c7 = models.CharField(max_length=500)
    c8 = models.CharField(max_length=500)
    c9 = models.CharField(max_length=500)
    c10 = models.CharField(max_length=500)
    id_evento = models.BigIntegerField()
    nome_formulario = models.CharField(max_length=150)
    data_cadastro = models.DateTimeField(auto_now=True)

class Submissao(models.Model):

    data = models.DateTimeField(auto_now=True)
    trabalho = models.FileField(null=True, upload_to='')
    id_evento = models.BigIntegerField()
    sessao = models.BigIntegerField()
    id_usuario = models.BigIntegerField()
    status = models.CharField(max_length=30)
    av1 = models.CharField(max_length=30)
    av2 = models.CharField(max_length=30)
    av3 = models.CharField(max_length=30, null=True)
    data_av1 = models.DateTimeField(null=True)
    data_av2 = models.DateTimeField(null=True)
    data_av3 = models.DateTimeField(null=True)

    def get_data_av1(self):
        return self.data_av1.strftime('%d/%m/%Y às %H:%M')
    def get_data_av2(self):
        return self.data_av2.strftime('%d/%m/%Y às %H:%M')
    def get_data_av3(self):
        return self.data_av3.strftime('%d/%m/%Y às %H:%M')
    def get_data(self):
        return self.data.strftime('%d/%m/%Y às %H:%M')

class Usuariocd(models.Model):

    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=300)
    cep = models.CharField(max_length=8)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=500)
    cidade = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)
    instituicao = models.CharField(max_length=150)
    cmp = models.CharField(max_length=3)
    categ = models.CharField(max_length=150)
    cinfo = models.CharField(max_length=3)
    gestor_plataforma = models.CharField(max_length=3)
    autor = models.CharField(max_length=3)
    avaliador = models.CharField(max_length=3)
    lider = models.CharField(max_length=3)
    id_usuario = models.BigIntegerField()
    contato = models.BigIntegerField(null=True)
    perfil = models.FileField(upload_to='')

class cpfteste(models.Model):

    cpf = CPFField('cpf')


class Sessoes(models.Model):

    data_criacao = models.DateTimeField(auto_now=True)
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    lider = models.CharField(max_length=150)
    tema = models.CharField(max_length=150)
    formulario = models.BigIntegerField()
    id_evento= models.BigIntegerField()

class Inscritos(models.Model):

    nome = models.CharField(max_length=150)
    cpf = models.BigIntegerField()
    id_evento = models.BigIntegerField()

class Avaliadores(models.Model):

    av1 = models.CharField(max_length=150)
    av2 = models.CharField(max_length=150)
    av3 = models.CharField(max_length=150)
    id_sessao = models.BigIntegerField()
    data_criacao = models.DateTimeField(auto_now=True)

class Criterios(models.Model):

    criterio = models.CharField(max_length=500)
    id_sessao = models.BigIntegerField()
    data_criacao = models.DateTimeField(auto_now=True)




