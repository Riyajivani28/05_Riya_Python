from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    DELIVERED = "delivered"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (DELIVERED, "Delivered"),
    ]

    customer_name = models.CharField(max_length=100)
    item = models.CharField(max_length=200)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} ({self.item})"
