# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Бренд', max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(verbose_name='Фотография', blank=True, upload_to='products/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(verbose_name='Бренд', null=True, related_name='products', to='shop.Brand'),
        ),
    ]
