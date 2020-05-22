# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='Дата обновления', auto_now=True)),
                ('active', models.BooleanField(verbose_name='Опубликовать', default=True)),
                ('post', models.ForeignKey(related_name='comments', to='shop.Product')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
