# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSizes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Размер одежды',
                'verbose_name_plural': 'Размеры одежды',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(null=True, to='shop.ProductSizes'),
        ),
    ]
