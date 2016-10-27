# -*- coding: utf -8 -*-
from django.db import models
from django.contrib.auth.models import User


class Materia(models.Model):

    nome = models.CharField(
        max_length=80,
        verbose_name='Nome da Matéria',
    )
    autor = models.ForeignKey(User)
    class Meta:

        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'

    def __unicode__(self):
        return self.nome
