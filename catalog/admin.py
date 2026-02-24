from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price_product', 'product_description', 'product_category', 'author')
    list_filter = ('product_category', 'author')
    search_fields = ('product_name', 'product_description', 'author')


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    search_fields = ('category_name',)
