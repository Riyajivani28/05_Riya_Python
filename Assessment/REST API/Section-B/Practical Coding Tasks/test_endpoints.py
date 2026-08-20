import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_ordering.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.models import Category, MenuItem, Order

client = Client()

# Retrieve or create test user and token
user = User.objects.get(username='testuser')
token = Token.objects.get(user=user)
auth_headers = {'HTTP_AUTHORIZATION': f'Token {token.key}'}

print("=== STARTING DRF API TESTS ===")

# 1. GET /api/categories/
res = client.get('/api/categories/')
print(f"1. GET /api/categories/ -> Status: {res.status_code}")
print(f"   Response: {res.json()}\n")
assert res.status_code == 200, f"Expected 200, got {res.status_code}"

# 2. Invalid price case: POST /api/menu-items/
invalid_item = {
    "name": "Invalid Price Item",
    "price": -50,
    "category": 1,
    "is_available": True
}
res = client.post('/api/menu-items/', data=json.dumps(invalid_item), content_type='application/json')
print(f"Invalid Price POST /api/menu-items/ -> Status: {res.status_code}")
print(f"   Response: {res.json()}\n")
assert res.status_code == 400, f"Expected 400, got {res.status_code}"

# 2. POST /api/menu-items/
new_item = {
    "name": "Garlic Bread",
    "price": "4.99",
    "category": 1,
    "is_available": True
}
res = client.post('/api/menu-items/', data=json.dumps(new_item), content_type='application/json')
print(f"2. POST /api/menu-items/ -> Status: {res.status_code}")
print(f"   Response: {res.json()}\n")
assert res.status_code == 201, f"Expected 201, got {res.status_code}"
item_id = res.json()['id']

# 3. GET /api/menu-items/
res = client.get('/api/menu-items/')
print(f"3. GET /api/menu-items/ -> Status: {res.status_code}")
print(f"   Response: {res.json()}\n")
assert res.status_code == 200, f"Expected 200, got {res.status_code}"

# 4. GET /api/menu-items/<id>/
res = client.get(f'/api/menu-items/{item_id}/')
print(f"4. GET /api/menu-items/{item_id}/ -> Status: {res.status_code}")
print(f"   Response: {res.json()}\n")
assert res.status_code == 200, f"Expected 200, got {res.status_code}"

# 5. PUT /api/menu-items/<id>/
update_item = {
    "name": "Garlic Bread with Cheese",
    "price": "5.99",
    "category": 1,
    "is_available": True
}
res = client.put(f'/api/menu-items/{item_id}/', data=json.dumps(update_item), content_type='application/json')
print(f"5. PUT /api/menu-items/{item_id}/ -> Status: {res.status_code}")
print(f"   Response: {res.json()}\n")
assert res.status_code == 200, f"Expected 200, got {res.status_code}"

# 6. DELETE /api/menu-items/<id>/
res = client.delete(f'/api/menu-items/{item_id}/')
print(f"6. DELETE /api/menu-items/{item_id}/ -> Status: {res.status_code}")
assert res.status_code == 204, f"Expected 204, got {res.status_code}"

# 7. POST /api/orders/
new_order = {
    "customer_name": "Grace",
    "item": "Margherita Pizza",
    "quantity": 3,
    "status": "pending"
}
res = client.post('/api/orders/', data=json.dumps(new_order), content_type='application/json')
print(f"7. POST /api/orders/ -> Status: {res.status_code}")
print(f"   Response: {res.json()}\n")
assert res.status_code == 201, f"Expected 201, got {res.status_code}"

# 8. GET /api/orders/ (Paginated)
res = client.get('/api/orders/')
print(f"8. GET /api/orders/ -> Status: {res.status_code}")
print(f"   Response: count={res.json().get('count')}, next={res.json().get('next')}, results_length={len(res.json().get('results', []))}\n")
assert res.status_code == 200, f"Expected 200, got {res.status_code}"

# 9. GET /api/orders/?status=pending
res = client.get('/api/orders/?status=pending')
print(f"9. GET /api/orders/?status=pending -> Status: {res.status_code}")
print(f"   Response: count={res.json().get('count')}, results={res.json().get('results')}\n")
assert res.status_code == 200, f"Expected 200, got {res.status_code}"

# 10. POST /api/my-orders/ WITH Token
my_order = {
    "item": "Cheeseburger",
    "quantity": 2,
    "status": "pending"
}
res = client.post('/api/my-orders/', data=json.dumps(my_order), content_type='application/json', **auth_headers)
print(f"10. POST /api/my-orders/ WITH Token -> Status: {res.status_code}")
print(f"    Response: {res.json()}\n")
assert res.status_code == 201, f"Expected 201, got {res.status_code}"

# 11. GET /api/my-orders/ WITH Token
res = client.get('/api/my-orders/', **auth_headers)
print(f"11. GET /api/my-orders/ WITH Token -> Status: {res.status_code}")
print(f"    Response: {res.json()}\n")
assert res.status_code == 200, f"Expected 200, got {res.status_code}"

# 12. GET /api/my-orders/ WITHOUT Token
res = client.get('/api/my-orders/')
print(f"12. GET /api/my-orders/ WITHOUT Token -> Status: {res.status_code}")
print(f"    Response: {res.json()}\n")
assert res.status_code == 401, f"Expected 401, got {res.status_code}"

print("=== ALL TESTS PASSED SUCCESSFULLY! ===")
