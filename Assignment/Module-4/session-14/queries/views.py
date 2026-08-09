from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.core.paginator import Paginator
from queries.models import Restaurant, Movie, Review, Category, Product
from queries.seeder import seed_all_data

def dashboard_view(request):
    # Ensure database has seed data
    seed_all_data()

    # 1. Restaurant filter: cuisine='Chinese' and rating > 4
    chinese_top_restaurants = Restaurant.objects.filter(cuisine='Chinese', rating__gt=4)
    all_restaurants = Restaurant.objects.all()

    # 2. User exclude: users who do NOT have 'gmail.com' in their email
    # Hint: Use the __contains lookup with exclude().
    non_gmail_users = User.objects.exclude(email__contains='gmail.com')
    all_users = User.objects.all()

    # 3. Movie annotate: count reviews for each Movie and display title + review count
    movies_annotated = Movie.objects.annotate(review_count=Count('reviews')).order_by('-review_count', 'title')

    # 4. Product & Category: select_related to fetch products with categories in a single query
    products_select_related = Product.objects.select_related('category').all()

    # 5. Flipkart-style products Q() filter: category='Electronics' OR price < 1000, paginated 5 per page
    q_filter = Q(category__name='Electronics') | Q(price__lt=1000)
    q_products_queryset = Product.objects.filter(q_filter).select_related('category').order_by('id')

    # Pagination: 5 products per page
    paginator = Paginator(q_products_queryset, 5)
    page_number = request.GET.get('page', 1)
    paginated_products = paginator.get_page(page_number)

    # Context with stats and queries
    context = {
        # Task 1
        'task1_results': chinese_top_restaurants,
        'task1_query': "Restaurant.objects.filter(cuisine='Chinese', rating__gt=4)",
        'all_restaurants_count': all_restaurants.count(),

        # Task 2
        'task2_results': non_gmail_users,
        'task2_query': "User.objects.exclude(email__contains='gmail.com')",
        'all_users_count': all_users.count(),

        # Task 3
        'task3_results': movies_annotated,
        'task3_query': "Movie.objects.annotate(review_count=Count('reviews'))",
        'all_movies_count': Movie.objects.count(),

        # Task 4
        'task4_results': products_select_related,
        'task4_query': "Product.objects.select_related('category').all()",
        'all_products_count': Product.objects.count(),

        # Task 5
        'task5_results': paginated_products,
        'task5_total_count': q_products_queryset.count(),
        'task5_query': "Product.objects.filter(Q(category__name='Electronics') | Q(price__lt=1000)).select_related('category')",
        'paginator': paginator,
    }

    return render(request, 'queries/dashboard.html', context)
