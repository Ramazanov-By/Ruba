from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name=u'Бренд')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=u'Фотография')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name


class ProductSizes(models.Model):
    title = models.CharField(max_length=30, verbose_name=u'Размер')

    class Meta:
        verbose_name = 'Размер одежды'
        verbose_name_plural = 'Размеры одежды'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name=u'Категория')
    brand = models.ForeignKey(Brand, related_name='products', verbose_name=u'Бренд', null=True)
    size = models.ForeignKey(ProductSizes, null=True, verbose_name=u'Размер')
    name = models.CharField(max_length=200, db_index=True, verbose_name=u'Название')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=u'Фотография')

    description = models.TextField(blank=True, verbose_name=u'Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=u'Цена')
    available = models.BooleanField(default=True, verbose_name=u'Опубликовать')
    new = models.BooleanField(default=False, verbose_name=u'Новый')
    sale = models.BooleanField(default=False, verbose_name=u'Распродажа')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Дата обновления')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',

                       args=[self.id, self.slug])


class ContactInfo(models.Model):
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=12, verbose_name=u'Телефон')
    description = models.TextField(blank=True, verbose_name=u'Описание')

    class Meta:
        verbose_name = 'Контакты компании'
        verbose_name_plural = 'Контакты компаний'

    def __str__(self):
        return self.email


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Заголовок')
    description = models.CharField(max_length=200, verbose_name=u'Описание')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=u'Фотография')

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Заголовок')
    description = models.CharField(max_length=250, verbose_name=u'Описание')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=u'Фотография')

    class Meta:
        verbose_name = 'Иформация о компании'
        verbose_name_plural = 'Иформация о компании'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Product, related_name='comments')
    name = models.CharField(max_length=80, verbose_name=u'Имя')
    email = models.EmailField()
    body = models.TextField(verbose_name=u'Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Дата обновления')
    active = models.BooleanField(default=True, verbose_name=u'Опубликовать')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)