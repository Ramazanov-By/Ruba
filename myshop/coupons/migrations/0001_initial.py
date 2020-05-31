# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(verbose_name='Дата активации', max_length=50, unique=True)),
                ('valid_from', models.DateTimeField(verbose_name='Дата окончания')),
                ('valid_to', models.DateTimeField(verbose_name='Код купона')),
                ('discount', models.IntegerField(verbose_name='% скидки', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(verbose_name='Активен')),
            ],
        ),
    ]
