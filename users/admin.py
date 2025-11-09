from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class User(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone_number', 'country', 'avatar', 'token')
    list_filter = ('email',)
    search_fields = ('email',)
