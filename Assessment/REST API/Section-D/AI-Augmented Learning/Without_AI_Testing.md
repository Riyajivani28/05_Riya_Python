AI Code Testing and Improvement

1. Exact Prompt Given to AI

Create a POST /api/orders/place/ endpoint using Django REST Framework. The endpoint should accept order details and create a new order. Return a success response when the order is placed successfully.

2. AI's Original Code

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def place_order(request):
    name = request.data.get('name')
    product = request.data.get('product')
    quantity = request.data.get('quantity')

    order = {
        "name": name,
        "product": product,
        "quantity": quantity
    }

    return Response({
        "message": "Order placed successfully",
        "order": order
    }, status=status.HTTP_201_CREATED)

Bug / Limitation Found

I tested the API manually without providing the quantity field. The AI's code still accepted the request and created an order with a missing quantity. This is a validation problem because quantity is required for placing an order.

My Corrected Version

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def place_order(request):
    name = request.data.get('name')
    product = request.data.get('product')
    quantity = request.data.get('quantity')

    if not name or not product or not quantity:
        return Response(
            {"error": "name, product and quantity are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    order = {
        "name": name,
        "product": product,
        "quantity": quantity
    }

    return Response(
        {
            "message": "Order placed successfully",
            "order": order
        },
        status=status.HTTP_201_CREATED
    )

3. What I Changed and Why

I tested the AI-generated code manually and found that required fields were not validated.
The API accepted a request even when the quantity was missing.
I added input validation for name, product, and quantity.
Now the API returns a proper 400 Bad Request response when required data is missing.