# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200527_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='structure',
            options={'verbose_name': 'Состав', 'verbose_name_plural': 'Составы'},
        ),
        migrations.AlterField(
            model_name='structure',
            name='title',
            field=models.CharField(verbose_name='Состав', max_length=30),
        ),
    ]
