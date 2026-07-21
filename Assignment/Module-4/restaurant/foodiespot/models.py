from django.db import models

# Create your models here.

class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    rating = models.FloatField()
    cuisine = models.ForeignKey(Cuisine,on_delete=models.CASCADE,related_name='restaurants')


