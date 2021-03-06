# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-29 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opiniao', models.IntegerField(verbose_name=b'Avaliacao')),
                ('assunto', models.CharField(blank=True, max_length=300, null=True, verbose_name=b'Coment\xc3\xa1rio sobre algum tema')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name=b'Coment\xc3\xa1rio sobre a Palestra')),
            ],
            options={
                'verbose_name': 'Avalia\xe7\xe3o',
                'verbose_name_plural': 'Avalia\xe7\xf5es',
            },
        ),
    ]
