from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random

from .serializers import ShoppingCartSerializer, CartProductSerializer
from baseDB.models import ShoppingCart, CartProduct, Product, DeliveryMethod


class ShoppingCartAPIView(APIView):
    def get(self, request, pk = None):
        try:
            shopping_cart = ShoppingCart.objects.get(cart_id = pk)
            serializer_shopping_cart= ShoppingCartSerializer(shopping_cart)
            return Response(serializer_shopping_cart.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'cart does not exists'}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk = None):
        serializer = CartProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        product = Product.objects.get(product_id = request.data["id_product"])
        shopping_cart = ShoppingCart.objects.get(cart_id = request.data["id_cart"])
        if shopping_cart.cart_delivery_cost  is None:
            shopping_cart.cart_delivery_cost = random.uniform(1.0, 10.0)
            shopping_cart.cart_delivery_discount = random.uniform(0.0, 5.0)
            shopping_cart.cart_total_cost = shopping_cart.cart_delivery_cost - shopping_cart.cart_delivery_discount + product.product_price
            product.product_stock -= 1
            shopping_cart.save()
            product.save()
        else:
            shopping_cart.cart_total_cost += product.product_price
            product.product_stock -= 1
            product.save()
            shopping_cart.save()

        return Response({"message: Product added successfully"}, status=status.HTTP_202_ACCEPTED)
        