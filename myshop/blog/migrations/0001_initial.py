# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(verbose_name='Фотография', blank=True, upload_to='blog/%Y/%m/%d')),
                ('publish', models.DateTimeField(verbose_name='Опубликовать', default=django.utils.timezone.now)),
                ('created', models.DateTimeField(verbose_name='Опубликовать', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='Дата обновления', auto_now=True)),
                ('status', models.CharField(verbose_name='Стус', max_length=10, default='draft', choices=[('draft', 'Draft'), ('published', 'Published')])),
                ('author', models.ForeignKey(related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('-publish',),
            },
        ),
    ]
