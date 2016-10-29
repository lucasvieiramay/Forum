# -*- coding: utf -8 -*-
from django.db import models

class Avaliacao(models.Model):

    opiniao = models.IntegerField(
        verbose_name='Avaliacao',
    )
    assunto = models.CharField(
        max_length = 300,
        verbose_name='Comentário sobre algum tema',
        null=True,
        blank=True,
    )
    comentario = models.TextField(
        null=True,
        blank=True,
        verbose_name='Comentário sobre a Palestra'
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = "Avaliações"

    def __unicode__(self):
        return self.opiniao
