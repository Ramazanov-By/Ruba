# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(verbose_name='Адрес', max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(verbose_name='Город', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(verbose_name='Дата создания', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(verbose_name='Имя', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(verbose_name='Фамилия', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(verbose_name='оплачено', default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(verbose_name='Почтовый индекс', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(verbose_name='Дата обновления', auto_now=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(verbose_name='Заказ', related_name='items', to='orders.Order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(verbose_name='Товар', related_name='order_items', to='shop.Product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество', default=1),
        ),
    ]
