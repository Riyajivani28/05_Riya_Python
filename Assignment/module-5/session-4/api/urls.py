from django.urls import path
from .views import PlaylistListView, OrderListView, CartView, TicketListView

urlpatterns = [
    path('playlists/', PlaylistListView.as_view(), name='playlist-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('cart/', CartView.as_view(), name='cart-view'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
]
