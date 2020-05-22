# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.CharField(verbose_name='Описание', max_length=200),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(verbose_name='Фотография', blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(verbose_name='Заголовок', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='Название', max_length=200, db_index=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(verbose_name='Телефон', max_length=12),
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(verbose_name='Опубликовать', default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(verbose_name='Категория', related_name='products', to='shop.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(verbose_name='Дата создания', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(verbose_name='Фотография', blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(verbose_name='Название', max_length=200, db_index=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='new',
            field=models.BooleanField(verbose_name='Новый', default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.BooleanField(verbose_name='Распродажа', default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(verbose_name='Размер', null=True, to='shop.ProductSizes'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(verbose_name='Дата обновления', auto_now=True),
        ),
        migrations.AlterField(
            model_name='productsizes',
            name='title',
            field=models.CharField(verbose_name='Размер', max_length=30),
        ),
    ]
