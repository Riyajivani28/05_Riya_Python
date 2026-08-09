from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()

    class Meta:
        ordering = ['-rating', 'name']

    def __str__(self):
        return f"{self.name} ({self.cuisine} - {self.rating} Stars)"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, blank=True)
    release_year = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.CharField(max_length=100, default="Anonymous")
    rating = models.IntegerField(default=5)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.reviewer}"


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
    badge = models.CharField(max_length=50, blank=True, default="Best Seller")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name} - ₹{self.price} ({self.category.name})"
