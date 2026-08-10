from django.db import models


class Cafe(models.Model):
    """
    Model representing a Cafe location.
    Used for nearby cafe search using Haversine formula.
    """
    name = models.CharField(max_length=200, help_text="Name of the cafe")
    address = models.CharField(max_length=300, help_text="Full address of the cafe")
    latitude = models.FloatField(help_text="Latitude coordinate")
    longitude = models.FloatField(help_text="Longitude coordinate")
    city = models.CharField(max_length=100, default="Rajkot", help_text="City name")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cafe"
        verbose_name_plural = "Cafes"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.city}"


class PickupPoint(models.Model):
    """
    Model representing a package pickup point.
    Used for nearest pickup-point search.
    """
    name = models.CharField(max_length=200, help_text="Name of the pickup point")
    address = models.CharField(max_length=300, help_text="Full address of the pickup point")
    latitude = models.FloatField(help_text="Latitude coordinate")
    longitude = models.FloatField(help_text="Longitude coordinate")
    city = models.CharField(max_length=100, default="Rajkot", help_text="City name")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pickup Point"
        verbose_name_plural = "Pickup Points"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.city}"
