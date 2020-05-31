from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250, verbose_name=u'Заголовок')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField(verbose_name=u'Текст')
    author = models.ForeignKey(User, related_name='blog_posts')
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, verbose_name=u'Фотография')
    publish = models.DateTimeField(default=timezone.now, verbose_name=u'Опубликовать')
    created = models.DateTimeField(auto_now_add=True,verbose_name=u'Опубликовать')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Дата обновления')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name=u'Стус')

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                              self.publish.strftime('%m'),
                              self.publish.strftime('%d'),
                              self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80, verbose_name=u'Имя')
    email = models.EmailField()
    body = models.TextField(verbose_name=u'Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Дата обновления')
    active = models.BooleanField(default=True, verbose_name=u'Опубликовать')

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
