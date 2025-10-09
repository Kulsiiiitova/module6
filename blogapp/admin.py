from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content',)
    list_filter = ('name',)
    search_fields = ('name', 'content',)