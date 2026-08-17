from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication,
    SessionAuthentication,
)

from .permissions import IsPremiumUser


class PlaylistListView(APIView):
    """
    1. Music App Playlist List Endpoint.
    Uses BasicAuthentication and IsAuthenticated permission.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        playlists = [
            {"id": 1, "title": "Top Hits 2026", "genre": "Pop", "tracks": 15},
            {"id": 2, "title": "Chill Lofi Beats", "genre": "Lo-Fi", "tracks": 25},
            {"id": 3, "title": "Acoustic Morning", "genre": "Acoustic", "tracks": 10},
        ]
        return Response({
            "message": f"Welcome {request.user.username}! Here are your playlists.",
            "playlists": playlists
        }, status=status.HTTP_200_OK)


class OrderListView(APIView):
    """
    2. Zomato-style Food Ordering App Endpoint.
    Uses TokenAuthentication and IsAuthenticated permission.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = [
            {"order_id": "ORD-101", "item": "Paneer Butter Masala", "restaurant": "Spicy Delights", "total": 350, "status": "Delivered"},
            {"order_id": "ORD-102", "item": "Chicken Biryani", "restaurant": "Biryani House", "total": 420, "status": "In Transit"},
        ]
        return Response({
            "user": request.user.username,
            "orders": orders
        }, status=status.HTTP_200_OK)

    def post(self, request):
        item = request.data.get("item", "Custom Food Order")
        quantity = request.data.get("quantity", 1)
        return Response({
            "message": "Order placed successfully!",
            "order": {"item": item, "quantity": quantity, "user": request.user.username}
        }, status=status.HTTP_201_CREATED)


class CartView(APIView):
    """
    3. Flipkart-style Shopping App Endpoint.
    Uses SessionAuthentication and IsAuthenticated permission.
    Only logged-in users can view/add items to cart.
    Unauthenticated users receive 403 Forbidden.
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart_items = [
            {"item_id": 501, "product_name": "Wireless Noise Canceling Headphones", "price": 2999, "quantity": 1},
            {"item_id": 502, "product_name": "Smart Fitness Watch", "price": 4999, "quantity": 1},
        ]
        return Response({
            "user": request.user.username,
            "cart": cart_items
        }, status=status.HTTP_200_OK)

    def post(self, request):
        item_name = request.data.get("product_name", "Sample Product")
        price = request.data.get("price", 999)
        return Response({
            "message": f"Added '{item_name}' to cart successfully!",
            "item": {"product_name": item_name, "price": price}
        }, status=status.HTTP_201_CREATED)


class TicketListView(APIView):
    """
    4. Tickets API Endpoint.
    Uses custom permission IsPremiumUser.
    Only users with is_premium=True can access this endpoint.
    """
    authentication_classes = [BasicAuthentication, TokenAuthentication, SessionAuthentication]
    permission_classes = [IsPremiumUser]

    def get(self, request):
        tickets = [
            {"ticket_id": "TCK-9901", "event": "Global Rock Festival 2026", "category": "VIP Lounge", "price": 5000},
            {"ticket_id": "TCK-9902", "event": "IPL Championship Final", "category": "Premium Suite", "price": 12000},
        ]
        return Response({
            "user": request.user.username,
            "is_premium": request.user.is_premium,
            "tickets": tickets
        }, status=status.HTTP_200_OK)
