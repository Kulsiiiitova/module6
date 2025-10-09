from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='название')
    category_description = models.CharField(max_length=200, verbose_name='описание')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['category_name',]


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='название')
    product_description = models.CharField(max_length=200, verbose_name='описание')
    product_picture = models.ImageField(upload_to='photos/', verbose_name='фотография')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='catalog', verbose_name='категория')
    price_product = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['product_name',]
