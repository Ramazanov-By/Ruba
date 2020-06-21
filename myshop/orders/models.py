from django.db import models
from shop.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=u'Имя')
    last_name = models.CharField(max_length=50, verbose_name=u'Фамилия')
    email = models.EmailField()
    phone = models.CharField(max_length=16, verbose_name=u'Номер', null=True)
    address = models.CharField(max_length=250, verbose_name=u'Адрес')
    postal_code = models.CharField(max_length=20, verbose_name=u'Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name=u'Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Дата обновления')
    paid = models.BooleanField(default=False, verbose_name=u'оплачено')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))

    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True)

    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', verbose_name=u'Заказ')
    product = models.ForeignKey(Product, related_name='order_items', verbose_name=u'Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name=u'Количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
