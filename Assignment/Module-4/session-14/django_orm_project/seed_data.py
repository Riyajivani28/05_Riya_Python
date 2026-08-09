import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm_project.settings')
django.setup()

from django.contrib.auth.models import User
from ormapp.models import Restaurant, Movie, Review, Category, Product

def populate_db():
    print("Starting database seeder...")

    # 1. Seed Restaurants
    Restaurant.objects.all().delete()
    restaurants = [
        Restaurant(name="Golden Dragon", cuisine="Chinese", rating=4.8),
        Restaurant(name="Dynasty Wok", cuisine="Chinese", rating=4.5),
        Restaurant(name="Panda Express", cuisine="Chinese", rating=4.2),
        Restaurant(name="Quick Chow", cuisine="Chinese", rating=3.8),
        Restaurant(name="Taj Mahal Dining", cuisine="Indian", rating=4.9),
        Restaurant(name="Bella Italia", cuisine="Italian", rating=4.6),
        Restaurant(name="Sakura Sushi", cuisine="Japanese", rating=4.7),
        Restaurant(name="Beijing House", cuisine="Chinese", rating=4.6),
        Restaurant(name="Spicy Bamboo", cuisine="Chinese", rating=4.1),
    ]
    Restaurant.objects.bulk_create(restaurants)
    print(f"Added {len(restaurants)} Restaurants.")

    # 2. Seed Users
    users_data = [
        ("riya_g", "riya@gmail.com", "Riya", "Jivani"),
        ("alex_g", "alex.smith@gmail.com", "Alex", "Smith"),
        ("john_g", "john.doe@gmail.com", "John", "Doe"),
        ("sarah_y", "sarah@yahoo.com", "Sarah", "Connor"),
        ("david_o", "david@outlook.com", "David", "Miller"),
        ("corporate", "contact@company.org", "Corporate", "User"),
        ("admin_user", "admin@enterprise.in", "Admin", "User"),
    ]
    for username, email, fname, lname in users_data:
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password="password123", first_name=fname, last_name=lname)
    print(f"Ensured {len(users_data)} Users exist.")

    # 3. Seed Movies & Reviews
    Movie.objects.all().delete()
    Review.objects.all().delete()

    inception = Movie.objects.create(name="Inception")
    interstellar = Movie.objects.create(name="Interstellar")
    dark_knight = Movie.objects.create(name="The Dark Knight")
    avatar = Movie.objects.create(name="Avatar")
    matrix = Movie.objects.create(name="The Matrix")

    reviews = [
        Review(movie=inception, review_text="Mind bending plot and awesome visual effects!", rating=5),
        Review(movie=inception, review_text="Hans Zimmer score is legendary.", rating=5),
        Review(movie=inception, review_text="Great thriller experience.", rating=4),

        Review(movie=interstellar, review_text="Emotional masterpiece about space and time.", rating=5),
        Review(movie=interstellar, review_text="Visually stunning scientific journey.", rating=5),
        Review(movie=interstellar, review_text="Unforgettable soundtrack.", rating=4),
        Review(movie=interstellar, review_text="Loved the black hole representation.", rating=5),
        Review(movie=interstellar, review_text="Pure cinematic magic.", rating=5),

        Review(movie=dark_knight, review_text="Heath Ledger Joker is iconic.", rating=5),
        Review(movie=dark_knight, review_text="Best superhero movie ever created.", rating=5),
        Review(movie=dark_knight, review_text="Brilliant dialogue and pacing.", rating=4),

        Review(movie=avatar, review_text="Revolutionary 3D visual spectacle.", rating=4),
    ]
    Review.objects.bulk_create(reviews)
    print(f"Added 5 Movies and {len(reviews)} Reviews.")

    # 4. Seed Category & Products
    Category.objects.all().delete()
    Product.objects.all().delete()

    electronics = Category.objects.create(name="Electronics")
    fashion = Category.objects.create(name="Fashion")
    home = Category.objects.create(name="Home & Kitchen")
    books = Category.objects.create(name="Books")

    products = [
        Product(name="Wireless Earbuds", category=electronics, price=899.00, rating=4.6),
        Product(name="Smart Watch Pro", category=electronics, price=2499.00, rating=4.8),
        Product(name="Gaming Mouse RGB", category=electronics, price=1599.00, rating=4.4),
        Product(name="USB-C Fast Cable", category=electronics, price=299.00, rating=4.2),
        Product(name="Bluetooth Speaker", category=electronics, price=1299.00, rating=4.7),
        Product(name="Mechanical Keyboard", category=electronics, price=3499.00, rating=4.9),
        Product(name="10000mAh Power Bank", category=electronics, price=799.00, rating=4.3),
        Product(name="Casual Cotton T-Shirt", category=fashion, price=499.00, rating=4.1),
        Product(name="Slim Fit Jeans", category=fashion, price=1499.00, rating=4.5),
        Product(name="Running Sports Shoes", category=fashion, price=2999.00, rating=4.7),
        Product(name="Stainless Water Bottle", category=home, price=599.00, rating=4.4),
        Product(name="LED Reading Lamp", category=home, price=850.00, rating=4.3),
        Product(name="Python Programming Guide", category=books, price=450.00, rating=4.9),
        Product(name="Django Web Development", category=books, price=650.00, rating=4.8),
    ]
    Product.objects.bulk_create(products)
    print(f"Added 4 Categories and {len(products)} Products.")
    print("Database seeding completed successfully!")

if __name__ == '__main__':
    populate_db()
