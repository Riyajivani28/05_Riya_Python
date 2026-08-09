from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from app.models import Order, Product, MovieReview, Playlist

class DynamicRBACTestCase(TestCase):
    def setUp(self):
        # Create groups
        self.seller_group = Group.objects.create(name="Seller")
        self.buyer_group = Group.objects.create(name="Buyer")
        self.critic_group = Group.objects.create(name="MovieCritic")
        self.fan_group = Group.objects.create(name="MovieFan")
        self.admin_group = Group.objects.create(name="Admin")

        # Create Users
        self.seller_user = User.objects.create_user(username='seller1', password='password123')
        self.seller_user.groups.add(self.seller_group)

        self.buyer_user = User.objects.create_user(username='buyer1', password='password123')
        self.buyer_user.groups.add(self.buyer_group)

        self.critic_user = User.objects.create_user(username='critic1', password='password123')
        self.critic_user.groups.add(self.critic_group)

        self.fan_user = User.objects.create_user(username='fan1', password='password123')
        self.fan_user.groups.add(self.fan_group)

        self.admin_staff_user = User.objects.create_user(username='admin_user', password='password123', is_staff=True)
        self.admin_staff_user.groups.add(self.admin_group)

        self.non_admin_staff_user = User.objects.create_user(username='staff_user', password='password123', is_staff=True)

        self.client = Client()

    def test_dynamic_product_crud_seller(self):
        """Seller can create, update, and delete products dynamically."""
        self.client.login(username='seller1', password='password123')
        
        # Create product
        post_response = self.client.post(reverse('post_product'), {
            'name': 'Dynamic Smartwatch',
            'description': 'Latest smartwatch with OLED screen',
            'price': '149.99'
        })
        self.assertRedirects(post_response, reverse('seller_dashboard'))
        self.assertTrue(Product.objects.filter(name='Dynamic Smartwatch').exists())

        product = Product.objects.get(name='Dynamic Smartwatch')

        # Edit product
        edit_response = self.client.post(reverse('edit_product', args=[product.id]), {
            'name': 'Dynamic Smartwatch Pro',
            'description': 'Updated description',
            'price': '199.99'
        })
        self.assertRedirects(edit_response, reverse('seller_dashboard'))
        product.refresh_from_db()
        self.assertEqual(product.name, 'Dynamic Smartwatch Pro')

        # Delete product
        del_response = self.client.post(reverse('delete_product', args=[product.id]))
        self.assertRedirects(del_response, reverse('seller_dashboard'))
        self.assertFalse(Product.objects.filter(id=product.id).exists())

    def test_dynamic_order_placement_and_isolation(self):
        """Buyer places order dynamically, updates order stats and enforces isolation."""
        product = Product.objects.create(
            seller=self.seller_user,
            name='Wireless Mouse',
            description='Ergonomic mouse',
            price=25.00
        )

        self.client.login(username='buyer1', password='password123')
        
        # Place order
        order_response = self.client.post(reverse('place_order_product', args=[product.id]), {
            'quantity': 2
        })
        self.assertRedirects(order_response, reverse('my_orders'))
        
        # Verify database record created
        self.assertTrue(Order.objects.filter(user=self.buyer_user, product_name='Wireless Mouse').exists())
        order = Order.objects.get(user=self.buyer_user, product_name='Wireless Mouse')
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.total_price(), 50.00)

        # Check order list view isolation
        my_orders_resp = self.client.get(reverse('my_orders'))
        self.assertContains(my_orders_resp, 'Wireless Mouse')

    def test_order_status_update_by_seller(self):
        """Seller can update status of an order placed for their product."""
        order = Order.objects.create(
            user=self.buyer_user,
            product_name='Test Item',
            quantity=1,
            price=10.00,
            status='Pending'
        )

        self.client.login(username='seller1', password='password123')
        resp = self.client.post(reverse('update_order_status', args=[order.id]), {
            'status': 'Out for Delivery'
        })
        self.assertRedirects(resp, reverse('seller_dashboard'))
        order.refresh_from_db()
        self.assertEqual(order.status, 'Out for Delivery')

    def test_movie_review_dynamic_crud(self):
        """MovieCritic can create, edit, and delete reviews dynamically."""
        self.client.login(username='critic1', password='password123')
        
        # Create review
        add_resp = self.client.post(reverse('add_review'), {
            'movie_name': 'Oppenheimer',
            'review_text': 'Masterpiece biopic',
            'rating': 5
        })
        self.assertRedirects(add_resp, reverse('movie_reviews'))
        review = MovieReview.objects.get(movie_name='Oppenheimer')

        # Edit review
        edit_resp = self.client.post(reverse('edit_review', args=[review.id]), {
            'movie_name': 'Oppenheimer (Extended)',
            'review_text': 'Updated review content',
            'rating': 5
        })
        self.assertRedirects(edit_resp, reverse('movie_reviews'))
        review.refresh_from_db()
        self.assertEqual(review.movie_name, 'Oppenheimer (Extended)')

        # Delete review
        del_resp = self.client.post(reverse('delete_review', args=[review.id]))
        self.assertRedirects(del_resp, reverse('movie_reviews'))
        self.assertFalse(MovieReview.objects.filter(id=review.id).exists())
