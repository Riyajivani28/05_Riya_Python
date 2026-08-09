from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Count, Sum, F, ExpressionWrapper, DecimalField
from .models import Order, Product, MovieReview, Playlist
from .forms import ProductForm, MovieReviewForm, PlaylistForm, OrderForm, OrderStatusUpdateForm
from .decorators import seller_required, buyer_required, group_required

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required
def dashboard_redirect(request):
    """
    Role-Based Dashboard routing based on user's Django Group using ORM filter.
    """
    user = request.user
    if user.groups.filter(name="Seller").exists():
        return redirect('seller_dashboard')
    elif user.groups.filter(name="Buyer").exists():
        return redirect('buyer_dashboard')
    elif user.groups.filter(name="MovieCritic").exists() or user.groups.filter(name="MovieFan").exists():
        return redirect('movie_reviews')
    else:
        if user.is_superuser:
            return redirect('seller_dashboard')
        return redirect('buyer_dashboard')

@login_required
@seller_required
def seller_dashboard(request):
    # Dynamic ORM querysets & statistics for Seller
    products = Product.objects.filter(seller=request.user).order_by('-created_at')
    
    # ORM Aggregations
    product_stats = products.aggregate(
        total_count=Count('id'),
        total_value=Sum('price')
    )
    product_count = product_stats['total_count'] or 0
    total_inventory_value = product_stats['total_value'] or 0.00

    # Orders related to this seller's products
    seller_product_names = list(products.values_list('name', flat=True))
    seller_orders = Order.objects.filter(product_name__in=seller_product_names).order_by('-ordered_at')
    pending_orders_count = seller_orders.filter(status='Pending').count()

    return render(request, 'seller_dashboard.html', {
        'products': products,
        'product_count': product_count,
        'total_inventory_value': total_inventory_value,
        'seller_orders': seller_orders,
        'pending_orders_count': pending_orders_count,
    })

@login_required
@buyer_required
def buyer_dashboard(request):
    # Dynamic ORM querysets & statistics for Buyer
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    
    # Dynamic ORM calculation of total orders and total spent
    order_stats = orders.aggregate(
        total_orders=Count('id'),
        total_spend=Sum(ExpressionWrapper(F('quantity') * F('price'), output_field=DecimalField()))
    )
    order_count = order_stats['total_orders'] or 0
    total_spent = order_stats['total_spend'] or 0.00
    delivered_count = orders.filter(status='Delivered').count()

    # Dynamic Marketplace Products available for order creation
    available_products = Product.objects.all().order_by('-created_at')

    return render(request, 'buyer_dashboard.html', {
        'orders': orders,
        'order_count': order_count,
        'total_spent': total_spent,
        'delivered_count': delivered_count,
        'available_products': available_products,
    })

@login_required
def my_orders(request):
    # Dynamic isolated order query for current user using ORM
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    
    order_stats = orders.aggregate(
        total_count=Count('id'),
        total_amount=Sum(ExpressionWrapper(F('quantity') * F('price'), output_field=DecimalField()))
    )
    total_count = order_stats['total_count'] or 0
    total_spent = order_stats['total_amount'] or 0.00

    return render(request, 'my_orders.html', {
        'orders': orders,
        'total_count': total_count,
        'total_spent': total_spent,
    })

@login_required
def place_order(request, product_id=None):
    # Dynamic order creation by Buyer
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity', 1))
        price = float(request.POST.get('price', 0.0))

        if product_id:
            product = get_object_or_404(Product, pk=product_id)
            product_name = product.name
            price = float(product.price)

        order = Order.objects.create(
            user=request.user,
            product_name=product_name,
            quantity=quantity,
            price=price,
            status='Pending'
        )
        messages.success(request, f"Order #{order.id} for '{order.product_name}' placed successfully!")
        return redirect('my_orders')

    return redirect('buyer_dashboard')

@login_required
def post_product(request):
    # Dynamic product posting by Seller
    if not (request.user.is_superuser or request.user.groups.filter(name="Seller").exists()):
        raise PermissionDenied("Buyers are not allowed to post products.")

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(request, f"Product '{product.name}' posted successfully!")
            return redirect('seller_dashboard')
    else:
        form = ProductForm()

    return render(request, 'post_product.html', {'form': form})

@login_required
def edit_product(request, pk):
    # Dynamic product updating by Seller
    product = get_object_or_404(Product, pk=pk)
    if not (request.user.is_superuser or (product.seller == request.user and request.user.groups.filter(name="Seller").exists())):
        raise PermissionDenied("You can only edit products that belong to you.")

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product '{product.name}' updated successfully!")
            return redirect('seller_dashboard')
    else:
        form = ProductForm(instance=product)

    return render(request, 'post_product.html', {'form': form, 'edit_mode': True, 'product': product})

@login_required
def delete_product(request, pk):
    # Dynamic product deletion by Seller
    product = get_object_or_404(Product, pk=pk)
    if not (request.user.is_superuser or (product.seller == request.user and request.user.groups.filter(name="Seller").exists())):
        raise PermissionDenied("You can only delete products that belong to you.")

    if request.method == 'POST':
        product_name = product.name
        product.delete()
        messages.success(request, f"Product '{product_name}' was deleted.")
        return redirect('seller_dashboard')

    return render(request, 'confirm_delete.html', {'object': product, 'type': 'Product', 'cancel_url': 'seller_dashboard'})

@login_required
def update_order_status(request, pk):
    # Dynamic Order Status Update for Sellers/Admins
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()
            messages.success(request, f"Order #{order.id} status updated to '{new_status}'!")
    return redirect('seller_dashboard')

@login_required
def movie_reviews(request):
    # Dynamic retrieval of reviews from database
    reviews = MovieReview.objects.all().order_by('-created_at')
    
    can_add = request.user.is_superuser or request.user.has_perm('app.add_moviereview') or request.user.groups.filter(name="MovieCritic").exists()
    can_edit = request.user.is_superuser or request.user.has_perm('app.change_moviereview') or request.user.groups.filter(name="MovieCritic").exists()

    return render(request, 'movie_reviews.html', {
        'reviews': reviews,
        'can_add': can_add,
        'can_edit': can_edit,
    })

@login_required
def add_review(request):
    can_add = request.user.is_superuser or request.user.has_perm('app.add_moviereview') or request.user.groups.filter(name="MovieCritic").exists()
    if not can_add:
        raise PermissionDenied("Only Movie Critics are allowed to add reviews.")

    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.created_by = request.user
            review.save()
            messages.success(request, f"Review for '{review.movie_name}' added successfully!")
            return redirect('movie_reviews')
    else:
        form = MovieReviewForm()

    return render(request, 'add_review.html', {'form': form})

@login_required
def edit_review(request, pk):
    can_edit = request.user.is_superuser or request.user.has_perm('app.change_moviereview') or request.user.groups.filter(name="MovieCritic").exists()
    if not can_edit:
        raise PermissionDenied("Only Movie Critics are allowed to edit reviews.")

    review = get_object_or_404(MovieReview, pk=pk)

    if request.method == 'POST':
        form = MovieReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, f"Review for '{review.movie_name}' updated successfully!")
            return redirect('movie_reviews')
    else:
        form = MovieReviewForm(instance=review)

    return render(request, 'edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, pk):
    can_edit = request.user.is_superuser or request.user.has_perm('app.change_moviereview') or request.user.groups.filter(name="MovieCritic").exists()
    if not can_edit:
        raise PermissionDenied("Only Movie Critics are allowed to delete reviews.")

    review = get_object_or_404(MovieReview, pk=pk)
    if request.method == 'POST':
        movie_name = review.movie_name
        review.delete()
        messages.success(request, f"Review for '{movie_name}' deleted successfully!")
        return redirect('movie_reviews')

    return render(request, 'confirm_delete.html', {'object': review, 'type': 'Movie Review', 'cancel_url': 'movie_reviews'})

def custom_permission_denied_view(request, exception=None):
    return render(request, 'permission_denied.html', status=403)
