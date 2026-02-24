from django.db import models


class BlogPost(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    content = models.CharField(max_length=200, verbose_name='содержимое')
    picture = models.ImageField(upload_to='photos_blog/', verbose_name='фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    views_counter = models.PositiveIntegerField(verbose_name='счетчик просмотров', default=0)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['name', ]
