from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.models import Order, Product, MovieReview, Playlist

class Command(BaseCommand):
    help = 'Creates Django Groups, assigns permissions, creates test users and populates sample data.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting setup of Groups, Permissions, and Test Data..."))

        # 1. Define and create Groups
        group_names = ['Seller', 'Buyer', 'MovieCritic', 'MovieFan', 'Admin']
        groups = {}
        for name in group_names:
            group, created = Group.objects.get_or_create(name=name)
            groups[name] = group
            if created:
                self.stdout.write(f"  Created Group: {name}")

        # 2. Assign model permissions to Groups
        # Get content types
        review_ct = ContentType.objects.get_for_model(MovieReview)
        product_ct = ContentType.objects.get_for_model(Product)
        order_ct = ContentType.objects.get_for_model(Order)
        playlist_ct = ContentType.objects.get_for_model(Playlist)

        # MovieCritic permissions
        critic_perms = Permission.objects.filter(
            content_type=review_ct,
            codename__in=['view_moviereview', 'add_moviereview', 'change_moviereview']
        )
        groups['MovieCritic'].permissions.set(critic_perms)

        # MovieFan permissions
        fan_perms = Permission.objects.filter(
            content_type=review_ct,
            codename__in=['view_moviereview']
        )
        groups['MovieFan'].permissions.set(fan_perms)

        # Seller permissions
        seller_perms = Permission.objects.filter(
            content_type=product_ct,
            codename__in=['view_product', 'add_product', 'change_product', 'delete_product']
        )
        groups['Seller'].permissions.set(seller_perms)

        # Buyer permissions
        buyer_perms = Permission.objects.filter(
            content_type=order_ct,
            codename__in=['view_order', 'add_order']
        )
        groups['Buyer'].permissions.set(buyer_perms)

        # Admin group permissions for Playlist
        admin_perms = Permission.objects.filter(
            content_type=playlist_ct,
            codename__in=['view_playlist', 'add_playlist', 'change_playlist', 'delete_playlist']
        )
        groups['Admin'].permissions.set(admin_perms)

        self.stdout.write(self.style.SUCCESS("  Permissions successfully assigned to Groups!"))

        # 3. Create Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword123')
            self.stdout.write(self.style.SUCCESS("  Created Superuser: admin (password: adminpassword123)"))

        # 4. Create Test Users & assign to Groups
        users_data = [
            ('seller1', 'Seller', False),
            ('buyer1', 'Buyer', False),
            ('critic1', 'MovieCritic', False),
            ('fan1', 'MovieFan', False),
            ('admin_user', 'Admin', True),     # Staff user IN Admin group
            ('staff_user', None, True),        # Staff user NOT in Admin group
        ]

        created_users = {}
        for username, group_name, is_staff in users_data:
            user, created = User.objects.get_or_create(username=username)
            user.set_password('password123')
            user.is_staff = is_staff
            user.save()

            if group_name and group_name in groups:
                user.groups.set([groups[group_name]])
            created_users[username] = user
            
            role_desc = group_name if group_name else ('Staff (No Admin Group)' if is_staff else 'No Role')
            self.stdout.write(f"  User '{username}' set up with role: {role_desc}")

        # 5. Populate Sample Data
        # Sample Orders for buyer1
        buyer = created_users['buyer1']
        if not Order.objects.filter(user=buyer).exists():
            Order.objects.create(user=buyer, product_name="Paneer Butter Masala", quantity=2, price=12.99, status="Delivered")
            Order.objects.create(user=buyer, product_name="Chicken Biryani Special", quantity=1, price=15.50, status="Out for Delivery")
            Order.objects.create(user=buyer, product_name="Mango Lassi", quantity=3, price=4.00, status="Processing")
            self.stdout.write("  Created sample orders for buyer1")

        # Sample Orders for another user to verify isolation
        seller = created_users['seller1']
        if not Order.objects.filter(user=seller).exists():
            Order.objects.create(user=seller, product_name="Cold Coffee", quantity=1, price=5.00, status="Delivered")

        # Sample Products for seller1
        if not Product.objects.filter(seller=seller).exists():
            Product.objects.create(seller=seller, name="Wireless Noise-Canceling Headphones", description="High quality bluetooth over-ear headphones.", price=199.99)
            Product.objects.create(seller=seller, name="Smart Fitness Watch V2", description="Waterproof smartwatch with heart rate monitoring.", price=89.50)
            self.stdout.write("  Created sample products for seller1")

        # Sample Movie Reviews by critic1
        critic = created_users['critic1']
        if not MovieReview.objects.filter(created_by=critic).exists():
            MovieReview.objects.create(created_by=critic, movie_name="Inception", review_text="A mind-bending masterpiece with phenomenal visual storytelling and score.", rating=5)
            MovieReview.objects.create(created_by=critic, movie_name="Interstellar", review_text="Visually spectacular and emotionally resonant space odyssey.", rating=5)
            self.stdout.write("  Created sample movie reviews by critic1")

        # Sample Playlists by admin_user
        admin_u = created_users['admin_user']
        if not Playlist.objects.filter(created_by=admin_u).exists():
            Playlist.objects.create(created_by=admin_u, name="Top Hits 2026", description="Best trending tracks of the year.")
            Playlist.objects.create(created_by=admin_u, name="Focus Coding Beats", description="Instrumental ambient music for programming.")
            self.stdout.write("  Created sample playlists by admin_user")

        self.stdout.write(self.style.SUCCESS("\nSETUP COMPLETE! All Groups, Permissions, Users, and Sample Data are ready."))
