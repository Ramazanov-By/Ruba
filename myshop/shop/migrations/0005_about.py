# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200519_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=50)),
                ('description', models.CharField(verbose_name='Описание', max_length=250)),
                ('image', models.ImageField(verbose_name='Фотография', blank=True, upload_to='products/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Иформация о компании',
                'verbose_name_plural': 'Иформация о компании',
            },
        ),
    ]
