import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodiehub.settings')
django.setup()

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# Create Standard User
user1, created1 = User.objects.get_or_create(
    username="user1",
    defaults={"is_premium": False}
)
if created1:
    user1.set_password("password123")
    user1.save()
token1, _ = Token.objects.get_or_create(user=user1)

# Create Premium User
user2, created2 = User.objects.get_or_create(
    username="premium_user",
    defaults={"is_premium": True}
)
if created2:
    user2.set_password("password123")
    user2.save()
token2, _ = Token.objects.get_or_create(user=user2)

print(f"Standard user created: user1 / password123 | Token: {token1.key}")
print(f"Premium user created: premium_user / password123 | Token: {token2.key}")
