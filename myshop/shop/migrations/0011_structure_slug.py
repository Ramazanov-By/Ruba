# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200527_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, null=True),
        ),
    ]
