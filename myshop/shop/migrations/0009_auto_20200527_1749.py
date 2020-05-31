# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20200525_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Характеристики', max_length=30)),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(verbose_name='Размер', blank=True, null=True, to='shop.ProductSizes'),
        ),
        migrations.AddField(
            model_name='product',
            name='structure',
            field=models.ManyToManyField(null=True, related_name='structure', to='shop.Structure'),
        ),
    ]
