from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

class Order(models.Model):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    DELIVERED = 'delivered'

    STATUS_CHOICES = [
        (PENDING, 'pending'),
        (CONFIRMED, 'confirmed'),
        (DELIVERED, 'delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
