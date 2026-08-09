from django.contrib import admin
from .models import Order, Product, MovieReview, Playlist

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_name', 'quantity', 'price', 'status', 'ordered_at')
    list_filter = ('status', 'ordered_at')
    search_fields = ('user__username', 'product_name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'seller', 'created_at')
    search_fields = ('name', 'seller__username')

@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'rating', 'created_by', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('movie_name', 'created_by__username')

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', 'created_at')

    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name="Admin").exists()

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name="Admin").exists()

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name="Admin").exists()

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name="Admin").exists()

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name="Admin").exists()
