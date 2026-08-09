from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['-rating', 'name']

    def __str__(self):
        return f"{self.name} ({self.cuisine} - {self.rating})"


class Movie(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return f"Review for {self.movie.name} - Rating {self.rating}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=4.5)
    image_url = models.CharField(max_length=500, blank=True, default="")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name} - ₹{self.price} ({self.category.name})"
