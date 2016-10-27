# -*- coding: utf -8 -*-
from django.db import models
from materias.models import Materia
from django.contrib.auth.models import User


class Pergunta(models.Model):

    titulo = models.CharField(
        max_length=200,
        verbose_name='Título da Pergunta',
    )
    comentario = models.TextField(
        verbose_name='Comentário sobre a pergunta',
        null=True,
        blank=True,
    )
    materia = models.ForeignKey(Materia)
    autor = models.ForeignKey(User)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = "Perguntas"

    def __unicode__(self):
        return self.titulo


class Resposta(models.Model):

    pergunta = models.ForeignKey(Pergunta)
    conteudo = models.TextField(
        verbose_name='Resposta',
    )
    autor = models.ForeignKey(User)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        permissions = (
            ("edit", "Pode editar todas respostas"),
            ("delete", "Pode apagar todas respostas"),
        )

    def __unicode__(self):
        return self.conteudo
