# -*- coding: utf -8 -*-
from django.shortcuts import render, redirect
from materias.models import Materia
from postagens.models import Pergunta, Resposta
from django.contrib.auth import authenticate
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from utils import senha_segura
from models import Avaliacao


# view para logar
def login_view(request):
    if request.POST:
        #pega user
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            context = {}
            context['erro'] = True
            return render(
                request,
                'login.html',
                context
            )

    return render(
        request,
        'login.html'
    )


# cria um user padrao
def create_user(request):
    if request.POST:
        #pega user
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #teste se username ja existe
        if User.objects.filter(username=username).exists():
            context = {}
            context['existe'] = True
            return render(
                request,
                'login.html',
                context
            )
        # testa se a senha e segura
        if senha_segura(password) == False:
            context = {}
            context['senha_fraca'] = True
            return render(
                request,
                'login.html',
                context
            )
        else:
            #Cria o usuário
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
            #Autentica para logar direto
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                return HttpResponseForbidden()

    return render(
        request,
        'login.html'
    )


# criar um user administrador
def create_user_administrador(request):
    if request.POST:
        #pega user
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #teste se username ja existe
        if User.objects.filter(username=username).exists():
            context = {}
            context['existe'] = True
            return render(
                request,
                'create_superuser.html',
                context
            )
        #Cria o usuário
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        #permissao de administrador
        user.is_staff=True
        user.save()
        #Autentica para logar direto
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return HttpResponseForbidden()

    return render(
        request,
        'create_superuser.html'
    )


#view para logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login/')
# lista todas as perguntas
def home(request):
    # Cria dicionario
    context = {}
    #nome do user logado
    context['username'] = request.user.username
    # Pega todas as materias e salva no dict
    context['materias'] = Materia.objects.all()
    # Pega todas as postagens
    context['perguntas'] = Pergunta.objects.all()
    return render(
        request,
        'home.html',
        context
    )

@login_required(login_url='/login/')
# Avaliacao da apresentacao
def avaliacao(request):
    # Cria dicionario
    context = {}
    if request.POST:
        #pega o que vier do form
        context['opiniao'] = request.POST.get("opiniao")
        context['assunto'] = request.POST.get("assunto")
        context['comentario'] = request.POST.get("comentario")
        #se tiver o campo obrigatorio
        if context['opiniao']:
            #Cria a avaliacao
            avaliacao = Avaliacao.objects.create(
                opiniao = context['opiniao'],
                assunto = context['assunto'],
                comentario = context['comentario'],
            )
            context['avaliacao_feita'] = True
            return render(
                request,
                'home.html',
                context
            )
    return render(
        request,
        'avaliacao.html',
        context
    )
