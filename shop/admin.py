from django.contrib import admin
from .models import Shop
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['productName', 'date']
    list_filter = ['date', 'productName']
    search_fields = ['productName']
    