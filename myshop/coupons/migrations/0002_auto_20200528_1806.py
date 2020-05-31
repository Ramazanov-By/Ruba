# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(verbose_name='Код купона', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(verbose_name='Дата активации'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(verbose_name='Дата окончания'),
        ),
    ]
