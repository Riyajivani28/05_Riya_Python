from django.contrib import admin
from .models import Category, MenuItem, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_available')
    list_filter = ('category', 'is_available')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'item', 'quantity', 'status', 'user')
    list_filter = ('status',)
