from django.contrib import admin
from .models import Cafe, PickupPoint


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'latitude', 'longitude', 'address', 'created_at')
    search_fields = ('name', 'city', 'address')
    list_filter = ('city', 'created_at')


@admin.register(PickupPoint)
class PickupPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'latitude', 'longitude', 'address', 'created_at')
    search_fields = ('name', 'city', 'address')
    list_filter = ('city', 'created_at')
