from django.contrib.auth.models import User
from queries.models import Restaurant, Movie, Review, Category, Product

def seed_all_data():
    # 1. Seed Restaurants
    if not Restaurant.objects.exists():
        Restaurant.objects.create(name="Golden Dragon", cuisine="Chinese", rating=4.8)
        Restaurant.objects.create(name="Panda Express", cuisine="Chinese", rating=4.3)
        Restaurant.objects.create(name="Dynasty Wok", cuisine="Chinese", rating=4.5)
        Restaurant.objects.create(name="Quick Chow", cuisine="Chinese", rating=3.8)
        Restaurant.objects.create(name="Taj Fine Dining", cuisine="Indian", rating=4.9)
        Restaurant.objects.create(name="Pasta Bella", cuisine="Italian", rating=4.6)
        Restaurant.objects.create(name="Tokyo Sushi", cuisine="Japanese", rating=4.7)

    # 2. Seed Users
    if User.objects.count() < 5:
        users_data = [
            ("riya_g", "riya@gmail.com", "Riya", "Jivani"),
            ("alex_g", "alex.smith@gmail.com", "Alex", "Smith"),
            ("john_g", "john.doe@gmail.com", "John", "Doe"),
            ("sarah_y", "sarah@yahoo.com", "Sarah", "Connor"),
            ("david_o", "david@outlook.com", "David", "Miller"),
            ("contact_c", "contact@company.org", "Corporate", "User"),
            ("admin_e", "admin@enterprise.in", "Admin", "User"),
        ]
        for username, email, fname, lname in users_data:
            if not User.objects.filter(username=username).exists():
                u = User.objects.create_user(username=username, email=email, password="password123")
                u.first_name = fname
                u.last_name = lname
                u.save()

    # 3. Seed Movies & Reviews
    if not Movie.objects.exists():
        inception = Movie.objects.create(title="Inception", genre="Sci-Fi", release_year=2010)
        interstellar = Movie.objects.create(title="Interstellar", genre="Sci-Fi", release_year=2014)
        dark_knight = Movie.objects.create(title="The Dark Knight", genre="Action", release_year=2008)
        avatar = Movie.objects.create(title="Avatar", genre="Sci-Fi", release_year=2009)
        matrix = Movie.objects.create(title="The Matrix", genre="Sci-Fi", release_year=1999)

        # Reviews
        Review.objects.create(movie=inception, reviewer="Alice", rating=5, comment="Mind bending masterpiece!")
        Review.objects.create(movie=inception, reviewer="Bob", rating=5, comment="Incredible soundtrack and visual effects.")
        Review.objects.create(movie=inception, reviewer="Charlie", rating=4, comment="Great plot!")
        Review.objects.create(movie=inception, reviewer="Dave", rating=5, comment="Best Nolan movie.")

        Review.objects.create(movie=interstellar, reviewer="Eve", rating=5, comment="Emotional and scientifically breathtaking.")
        Review.objects.create(movie=interstellar, reviewer="Frank", rating=5, comment="Zimmer score is unreal.")
        Review.objects.create(movie=interstellar, reviewer="Grace", rating=4, comment="Stunning visuals.")
        Review.objects.create(movie=interstellar, reviewer="Hank", rating=5, comment="Loved Hans Zimmer's score.")
        Review.objects.create(movie=interstellar, reviewer="Ivy", rating=5, comment="Unforgettable experience.")

        Review.objects.create(movie=dark_knight, reviewer="Jack", rating=5, comment="Joker performance was legendary.")
        Review.objects.create(movie=dark_knight, reviewer="Karen", rating=5, comment="Best superhero film ever.")
        Review.objects.create(movie=dark_knight, reviewer="Leo", rating=4, comment="Classic cinematic masterpiece.")

        Review.objects.create(movie=avatar, reviewer="Mona", rating=4, comment="Revolutionary 3D visual spectacle.")
        # Matrix left with 0 reviews to show 0 review count in annotate()

    # 4. Seed Category & Products
    if not Category.objects.exists():
        electronics = Category.objects.create(name="Electronics")
        fashion = Category.objects.create(name="Fashion")
        home = Category.objects.create(name="Home & Kitchen")
        books = Category.objects.create(name="Books")

        products_data = [
            ("Wireless Bluetooth Earbuds", electronics, 899.00, "Top Deal"),
            ("Smart Fitness Watch", electronics, 2499.00, "Trending"),
            ("Gaming Headphones HD", electronics, 1599.00, "Popular"),
            ("USB-C Fast Charging Cable", electronics, 299.00, "Budget Choice"),
            ("Portable Bluetooth Speaker", electronics, 1299.00, "High Rating"),
            ("Mechanical RGB Keyboard", electronics, 3499.00, "Premium"),
            ("10000mAh Power Bank", electronics, 799.00, "Must Have"),
            ("Casual Cotton T-Shirt", fashion, 499.00, "Hot Deal"),
            ("Slim Fit Denim Jeans", fashion, 1499.00, "Stylish"),
            ("Running Sports Shoes", fashion, 2999.00, "Popular"),
            ("Stainless Steel Water Bottle", home, 599.00, "Eco Friendly"),
            ("LED Desk Reader Lamp", home, 850.00, "Best Value"),
            ("Python Programming Mastery", books, 450.00, "Bestseller"),
            ("Django Web Development Guide", books, 650.00, "Recommended"),
        ]

        for name, category, price, badge in products_data:
            Product.objects.create(name=name, category=category, price=price, badge=badge)
