from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('criarevento/', views.criarevento),
    path('submetertrabalho/', views.submetertrabalho),
    path('login/', views.logando),
    path('novocadastro/', views.novocadastro),
    path('teste/', views.teste),
    path('novocadastrar/', views.novocadastrar),
    path('logar/', views.logar),
    path('meuperfil/', views.meuperfil),
    path('attperfil/', views.attperfil),
    path('gerenciarevento/', views.gerenciarevento),
    path('editarevento/', views.editarevento),
    path('alterarevento/', views.alterarevento),
    path('addsessao/', views.addsessao),
    path('criarsessao/', views.criarsessao),
    path('inscrever/', views.inscrever),
    path('inscricao/', views.inscricao),
    path('submeter/', views.submeter),
    path('submetidos/', views.submetidos),
    path('editarsessao/', views.editarsessao),
    path('addavaliadores/', views.addavaliadores),
    path('addcriterio/', views.addcriterio),
    path('avaliartrabalho/', views.avaliartrabalho),
    path('enviaravaliacao/', views.enviaravaliacao),
    path('avaliados/', views.avaliados),
    path('principal/', views.principal),
    path('submissoes/', views.submissoes),
    path('criandoevento/', views.criandoevento),
    path('', views.semlink),
    path('formularios/', views.formulario),
    path('enviaravaliador/', views.enviaravaliador),
    path('pontuartrabalho/', views.pontuartrabalho),
    path('avaliarformulario/', views.avaliarformulario),
    path('editarformulario/', views.editarformulario),
    path('salvarformulario/', views.salvarformulario),
    path('arquivos/', views.arquivos),
    path('deslogar/', views.deslogar),
    path('verjs/', views.verjs),
    path('eviaremail/', views.eviaremail),
    path('usuarios/', views.usuarios),
    path('inscreveruser/', views.inscreveruser),
    path('tainscrito/', views.tainscrito),
    path('cformulario/', views.formularios),
    path('criarformulario/', views.criarformulario),
    path('eventos/', views.eventos),
    path('atualizarsenha/', views.attsenha),
    path('mudarsenha/', views.mudarsenha),
    path('editsessao/', views.editsessao),
    path('formavaliado/', views.formavaliado)

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)