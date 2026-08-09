from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Restaurant, Movie, Review, Category, Product

# --- HOME DASHBOARD ---
def dashboard_view(request):
    # Overview Stats
    stats = {
        'total_restaurants': Restaurant.objects.count(),
        'total_users': User.objects.count(),
        'total_movies': Movie.objects.count(),
        'total_reviews': Review.objects.count(),
        'total_products': Product.objects.count(),
    }

    # Task 1: Restaurant Filter
    t1_query = "Restaurant.objects.filter(cuisine='Chinese', rating__gt=4)"
    t1_results = Restaurant.objects.filter(cuisine='Chinese', rating__gt=4)

    # Task 2: User Exclude
    t2_query = "User.objects.exclude(email__contains='gmail.com')"
    t2_results = User.objects.exclude(email__contains='gmail.com')

    # Task 3: Movie Annotate
    t3_query = "Movie.objects.annotate(review_count=Count('reviews'))"
    t3_results = Movie.objects.annotate(review_count=Count('reviews'))

    # Task 4: Select Related
    t4_query = "Product.objects.select_related('category')"
    t4_results = Product.objects.select_related('category')[:6]

    # Task 5: Q() + Paginator
    t5_query = "Product.objects.filter(Q(category__name='Electronics') | Q(price__lt=1000))"
    t5_qs = Product.objects.filter(Q(category__name='Electronics') | Q(price__lt=1000)).select_related('category')
    t5_paginator = Paginator(t5_qs, 5)
    t5_page = t5_paginator.get_page(request.GET.get('page', 1))

    context = {
        'stats': stats,
        't1_query': t1_query,
        't1_results': t1_results,
        't2_query': t2_query,
        't2_results': t2_results,
        't3_query': t3_query,
        't3_results': t3_results,
        't4_query': t4_query,
        't4_results': t4_results,
        't5_query': t5_query,
        't5_results': t5_page,
    }
    return render(request, 'dashboard.html', context)


# --- RESTAURANT MANAGEMENT ---
def restaurant_list_view(request):
    search_query = request.GET.get('q', '')
    filter_mode = request.GET.get('filter', 'task') # 'task' or 'all'

    if filter_mode == 'task':
        query_code = "Restaurant.objects.filter(cuisine='Chinese', rating__gt=4)"
        restaurants = Restaurant.objects.filter(cuisine='Chinese', rating__gt=4)
    else:
        query_code = "Restaurant.objects.all()"
        restaurants = Restaurant.objects.all()

    if search_query:
        restaurants = restaurants.filter(
            Q(name__icontains=search_query) | Q(cuisine__icontains=search_query)
        )
        query_code += f".filter(Q(name__icontains='{search_query}') | Q(cuisine__icontains='{search_query}'))"

    return render(request, 'restaurant.html', {
        'restaurants': restaurants,
        'query_code': query_code,
        'search_query': search_query,
        'filter_mode': filter_mode
    })


def restaurant_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        if name and cuisine and rating:
            Restaurant.objects.create(name=name, cuisine=cuisine, rating=float(rating))
            messages.success(request, f"Restaurant '{name}' added successfully!")
            return redirect('restaurants')
    return render(request, 'restaurant_form.html', {'title': '➕ Add Restaurant'})


def restaurant_edit_view(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.name = request.POST.get('name')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = float(request.POST.get('rating'))
        restaurant.save()
        messages.success(request, f"Restaurant '{restaurant.name}' updated successfully!")
        return redirect('restaurants')
    return render(request, 'restaurant_form.html', {'restaurant': restaurant, 'title': '✏️ Edit Restaurant'})


def restaurant_delete_view(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    name = restaurant.name
    restaurant.delete()
    messages.success(request, f"Restaurant '{name}' deleted successfully!")
    return redirect('restaurants')


# --- USER MANAGEMENT ---
def user_list_view(request):
    tab = request.GET.get('tab', 'exclude')
    search_q = request.GET.get('q', '')

    if tab == 'exclude':
        query_code = "User.objects.exclude(email__contains='gmail.com')"
        users = User.objects.exclude(email__contains='gmail.com')
    elif tab == 'gmail':
        query_code = "User.objects.filter(email__contains='gmail.com')"
        users = User.objects.filter(email__contains='gmail.com')
    else:
        query_code = "User.objects.all()"
        users = User.objects.all()

    if search_q:
        users = users.filter(Q(username__icontains=search_q) | Q(first_name__icontains=search_q) | Q(email__icontains=search_q))

    return render(request, 'users.html', {
        'users': users,
        'query_code': query_code,
        'active_tab': tab,
        'search_q': search_q
    })


# --- MOVIE & REVIEW MANAGEMENT ---
def movie_list_view(request):
    query_code = "Movie.objects.annotate(review_count=Count('reviews'))"
    movies = Movie.objects.annotate(review_count=Count('reviews')).order_by('-review_count', 'name')

    return render(request, 'movies.html', {
        'movies': movies,
        'query_code': query_code
    })


def movie_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Movie.objects.create(name=name)
            messages.success(request, f"Movie '{name}' added successfully!")
            return redirect('movies')
    return render(request, 'movie_form.html')


def review_add_view(request):
    movies = Movie.objects.all()
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating', 5)
        if movie_id and review_text:
            movie = get_object_or_404(Movie, pk=movie_id)
            Review.objects.create(movie=movie, review_text=review_text, rating=int(rating))
            messages.success(request, f"Review added for movie '{movie.name}'!")
            return redirect('movies')
    return render(request, 'review_form.html', {'movies': movies})


# --- CATEGORY & PRODUCT MANAGEMENT ---
def product_list_view(request):
    query_code = "Product.objects.select_related('category')"
    category_id = request.GET.get('category')
    search_q = request.GET.get('q', '')

    products = Product.objects.select_related('category').all()

    if category_id:
        products = products.filter(category_id=category_id)
        query_code += f".filter(category_id={category_id})"

    if search_q:
        products = products.filter(name__icontains=search_q)

    categories = Category.objects.all()

    return render(request, 'products.html', {
        'products': products,
        'categories': categories,
        'query_code': query_code,
        'selected_category': category_id,
        'search_q': search_q
    })


def category_add_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            messages.success(request, f"Category '{name}' added successfully!")
            return redirect('products')
    return render(request, 'category_form.html')


def product_add_view(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category_id')
        price = request.POST.get('price')
        rating = request.POST.get('rating', 4.5)
        if name and category_id and price:
            category = get_object_or_404(Category, pk=category_id)
            Product.objects.create(name=name, category=category, price=float(price), rating=float(rating))
            messages.success(request, f"Product '{name}' added successfully!")
            return redirect('products')
    return render(request, 'product_form.html', {'categories': categories})


# --- FLIPKART SHOPPING PAGE (Q FILTER & PAGINATOR) ---
def flipkart_shopping_view(request):
    q_active = request.GET.get('q_filter', 'on') # 'on' or 'off'
    search_q = request.GET.get('q', '')
    cat_filter = request.GET.get('category', '')

    if q_active == 'on':
        query_code = "Product.objects.filter(Q(category__name='Electronics') | Q(price__lt=1000)).select_related('category')"
        products_qs = Product.objects.filter(Q(category__name='Electronics') | Q(price__lt=1000)).select_related('category')
    else:
        query_code = "Product.objects.select_related('category').all()"
        products_qs = Product.objects.select_related('category').all()

    if cat_filter:
        products_qs = products_qs.filter(category_id=cat_filter)

    if search_q:
        products_qs = products_qs.filter(name__icontains=search_q)

    # Paginator: Exactly 5 products per page
    paginator = Paginator(products_qs, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    return render(request, 'flipkart.html', {
        'products': page_obj,
        'query_code': query_code,
        'q_active': q_active,
        'categories': categories,
        'selected_cat': cat_filter,
        'search_q': search_q
    })
