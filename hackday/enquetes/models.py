# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Enquete(models.Model):

	pergunta = models.CharField(
		max_length = 100,
		verbose_name= 'Nome da Pergunta'
	)
	autor = models.ForeignKey(User)
	opcao1 = models.CharField(
		max_length = 100,
		verbose_name= 'Opção 1',
		blank = True,
		null = True
	)
	opcao2 = models.CharField(
		max_length = 100,
		verbose_name= 'Opção 2',
		blank = True,
		null = True
	)
	opcao3 = models.CharField(
		max_length = 100,
		verbose_name= 'Opção 3',
		blank = True,
		null = True
	)
