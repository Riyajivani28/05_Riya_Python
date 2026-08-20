from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer

class PlaceOrderAPIView(APIView):
    def post(self, request):
        quantity = request.data.get('quantity')

        # Validate quantity: must be an integer and greater than 0
        if type(quantity) is not int or quantity <= 0:
            return Response(
                {"error": "Quantity must be a positive integer."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
