# -*- coding: utf -8 -*-
from django.shortcuts import render
from postagens.models import Pergunta
from models import Materia
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
# cadastra materia
def cadastra_materia(request):
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
        nome = request.POST.get("nome")
        autor = request.user
        # assegura que veio os campos obrigatorios
        if nome:
            # cria a Materia
            materia = Materia.objects.create(
                nome=nome,
                autor=autor
            )
            return redirect('/')

    return render(
        request,
        'cadastra_materia.html',
        context
    )


@login_required(login_url='/login/')
# lista as perguntas de cada materia
def perguntas_materia(request, materia):
    # Cria dicionario
    context = {}
    # Pega todas as materias para o menu
    context['materias'] = Materia.objects.all()
    # Pega a materia passada por parametro
    materia = Materia.objects.get(id=int(materia))
    context['materia'] = materia
    # Pega as perguntas dessa materia
    context['perguntas'] = Pergunta.objects.filter(materia=materia)
    return render(
        request,
        'materia.html',
        context
    )
