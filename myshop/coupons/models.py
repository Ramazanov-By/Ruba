from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name=u'Код купона')
    valid_from = models.DateTimeField(verbose_name=u'Дата активации')
    valid_to = models.DateTimeField(verbose_name=u'Дата окончания')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name=u'% скидки')
    active = models.BooleanField(verbose_name=u'Активен')

    def __str__(self):
        return self.code