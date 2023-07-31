from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random

from .serializer import ShoppingCartSerializer, CartProductSerializer
from baseDB.models import ShoppingCart, CartProduct, Product, DeliveryMethod

class ShoppingProductAPIView(APIView):
    def get(self, request, pk = None):
        try:
            shopping_cart = ShoppingCart.objects.get(cart_id = pk)
            serializer_shopping_cart= ShoppingCartSerializer(shopping_cart)
            return Response(serializer_shopping_cart.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'cart does not exists'}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk = None):
       try:
            products = CartProduct.objects.create(id_cart = ShoppingCart.objects.get(cart_id = request.data['id_cart']), id_product = Product.objects.get(product_id = request.data['id_product']))
            products.save()
            cart = ShoppingCart.objects.get(cart_id = pk)
            cart.cart_delivery_method = DeliveryMethod.objects.get(delivery_method_id = request.data["delivery_method"])
            product = Product.objects.get(product_id = request.data["id_product"])
            delivery = cart.cart_delivery_cost = random.uniform(1.0, 20.0 )
            discount = cart.cart_delivery_discount = random.uniform(0.0, 10.0)
            cart.cart_total_cost += delivery - discount + product.product_price
            product.product_stock -= 1
            product.save()
            cart.save()
            return Response({"message": 'product added succesfully'}, status = status.HTTP_202_ACCEPTED)
       except:
            return Response({"error": 'something wrong'}, status= status.HTTP_400_BAD_REQUEST)



