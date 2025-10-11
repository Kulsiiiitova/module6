from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price_product', 'product_description', 'product_category',)
    list_filter = ('product_category',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    search_fields = ('category_name',)
