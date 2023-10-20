# REST_FRAMEWORK
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import ProductModelSerializaer
from baseDB.models import Product


class ProductsAPiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductModelSerializaer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsCategoryApiView(APIView):
    error_message = {"error": "There are not products"}

    def get(self, request, category):
        products = Product.objects.filter(
            product_category__category_name=category)
        if products:
            serializer = ProductModelSerializaer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(error_message, status=status.HTTP_404_NOT_FOUND)


class OneProductCategoryApiView(APIView):
    error_message = {'error': 'There is not product'}

    def get(self, request, pk=None):
        product = Product.objects.filter(product_id=pk).first()
        if product:
            serializer = ProductModelSerializaer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(error_message, status=status.HTTP_404_NOT_FOUND)
