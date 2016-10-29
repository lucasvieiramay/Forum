"""hackday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'forum.views.home'),
    url(r'^login/$', 'forum.views.login_view'),
    url(r'^logout/$', 'forum.views.logout_view'),
    url(r'^create/user/$', 'forum.views.create_user'),
    url(r'^create/administrador/$', 'forum.views.create_user_administrador'),
    url(r'^materia/(?P<materia>\w+)/$', 'materias.views.perguntas_materia'),
    url(r'^pergunta/(?P<pergunta>\w+)/$', 'postagens.views.pagina_pergunta'),
    url(r'^cadastra/pergunta/$', 'postagens.views.cadastra_pergunta'),
    url(r'^edita/pergunta/(?P<pergunta>\w+)/$', 'postagens.views.edita_pergunta'),
    url(r'^edita/resposta/(?P<resposta>\w+)/$', 'postagens.views.edita_resposta'),
    url(r'^apaga/pergunta/(?P<pergunta>\w+)/$', 'postagens.views.apaga_pergunta'),
    url(r'^apaga/resposta/(?P<resposta>\w+)/$', 'postagens.views.apaga_resposta'),
    url(r'^cadastra/materia/$', 'materias.views.cadastra_materia'),
    url(r'^cadastra/resposta/(?P<pergunta>\w+)/$', 'postagens.views.cadastra_resposta'),
    url(r'^avalie/$', 'forum.views.avaliacao'),
]
