# -*- coding: utf -8 -*-
from django.shortcuts import render
from models import Pergunta, Resposta
from models import Materia
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required(login_url='/login/')
# Cadastra uma pergunta no forum
def cadastra_pergunta(request):
    # Cria dicionario
    context = {}
    # Pega todas as materias para o menu
    context['materias'] = Materia.objects.all()
    # se for post
    if request.POST:
        """
        pega os dados do form que vieram via post
        obs: eu sei que o django tem o forms pra facilitar
        mas prefiro criar os meus proprios e usar os meus
        validadores e mascaras.
        """
        titulo = request.POST.get("titulo")
        comentario = request.POST.get("comentario")
        materia = request.POST.get("materia")
        materia = Materia.objects.get(id=materia)
        autor = request.user
        # assegura que veio os campos obrigatorios
        if titulo and materia:
            # cria a Pergunta
            pergunta = Pergunta.objects.create(
                titulo=titulo,
                comentario=comentario,
                materia=materia,
                autor=autor
            )
            return redirect('/')

    return render(
        request,
        'cadastra_pergunta.html',
        context
    )


@login_required(login_url='/login/')
# Edita uma pergunta no forum
def edita_pergunta(request, pergunta):
    # Cria dicionario
    context = {}
    # Pega todas as materias para o menu
    context['materias'] = Materia.objects.all()
    context['edit'] = True
    context['pergunta'] = Pergunta.objects.get(id = int(pergunta))
    if request.POST:
        user = request.user
        pergunta = context['pergunta']
        if user.is_staff or pergunta.autor == user:
            titulo = request.POST.get("titulo")
            comentario = request.POST.get("comentario")
            materia = request.POST.get("materia")
            materia = Materia.objects.get(id=materia)
            autor = request.user
            # assegura que veio os campos obrigatorios
            if titulo and materia:
                # update na Pergunta
                pergunta.titulo = titulo
                pergunta.comentario = comentario
                pergunta.materia = materia
                pergunta.updated_at = datetime.now()
                pergunta.save()
                return redirect('/')

        else:
            return HttpResponseForbidden()


    return render(
        request,
        'cadastra_pergunta.html',
        context
    )


@login_required(login_url='/login/')
# Edita Resposta
def edita_resposta(request, resposta):
    # Cria dicionario
    context = {}
    # Pega todas as materias para o menu
    context['materias'] = Materia.objects.all()
    #pega a resposta passada pela url
    resposta = Resposta.objects.get(id = int(resposta))
    #salva no dict pra renderizar no template
    context['resposta'] = resposta
    if request.POST:
        conteudo = request.POST.get("resposta")
        autor = request.user
        # assegura que veio os campos obrigatorios
        if resposta:
            # edita a resposta
            resposta.conteudo = conteudo
            resposta.updated_at = datetime.now()
            resposta.save()
            return redirect('/pergunta/%s' % (resposta.pergunta.id))

    return render(
        request,
        'edita_resposta.html',
        context
    )


@login_required(login_url='/login/')
# Apaga Pergunta
def apaga_pergunta(request, pergunta):
    pergunta = Pergunta.objects.get(id = int(pergunta))
    autor = pergunta.autor
    logado = request.user
    #Se o autor for o usuario logado
    #ou o usuario logado for staff(adm)
    if autor == logado or logado.is_staff:
        pergunta.delete()
        return redirect('/')
    #senao 403
    else:
        return HttpResponseForbidden()
    """
    Sei que poderia fazer todos os testes de permissao em uma linha
    mas acho ruim pra quem for ler, de visualizar e entender.
    """


@login_required(login_url='/login/')
# Apaga Resposta
def apaga_resposta(request, resposta):
    resposta = Resposta.objects.get(id = int(resposta))
    autor = resposta.autor
    logado = request.user
    #Se o autor for o usuario logado
    #ou o usuario logado for staff(adm)
    if autor == logado or logado.is_staff:
        resposta.delete()
        return redirect('/pergunta/%s/' % (resposta.pergunta.id))
    #senao 403
    else:
        return HttpResponseForbidden()


@login_required(login_url='/login/')
# Pagina da pergunta que vier passada por parametro
def pagina_pergunta(request, pergunta):
    # Cria dicionario
    context = {}
    # Pega todas as materias para o menu
    context['materias'] = Materia.objects.all()
    # Pega a materia passada por parametro
    pergunta = Pergunta.objects.get(id=int(pergunta))
    context['pergunta'] = pergunta
    context['respostas'] = Resposta.objects.filter(pergunta=pergunta)

    #Testa permissoes
    if pergunta.autor == request.user:
        context['autor_pergunta'] = True
    elif request.user.is_staff:
        context['admin'] = True

    return render(
        request,
        'pergunta.html',
        context
    )


@login_required(login_url='/login/')
# Responder Pergunta
def cadastra_resposta(request, pergunta):
    # Cria dicionario
    context = {}
    # Pega todas as materias para o menu
    context['materias'] = Materia.objects.all()
    # se for post
    if request.POST:
        resposta = request.POST.get("resposta")
        pergunta = Pergunta.objects.get(id=int(pergunta))
        autor = request.user
        # assegura que veio os campos obrigatorios
        if resposta and pergunta:
            # cria a Resposta
            resposta = Resposta.objects.create(
                pergunta=pergunta,
                conteudo=resposta,
                autor=autor
            )
            return redirect('/pergunta/%s' % (pergunta.id))

    return render(
        request,
        'pergunta.html',
        context
    )
