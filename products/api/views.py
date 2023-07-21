from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from .serializer import ProductModelSerializaer
from baseDB.models import Product

class ProductsAPiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductModelSerializaer(products, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProductsCategoryApiView(APIView):
    def get(self, request, category):
            products = Product.objects.filter(product_category__category_name = category)
            if products:
                serializer = ProductModelSerializaer(products, many = True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "There are not products"}, status=status.HTTP_404_NOT_FOUND)
    
class OneProductCategoryApiView(APIView):
    def get(self, request, pk= None):
        try:
            product = Product.objects.get(product_id = pk)
            serializer = ProductModelSerializaer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'There is not product'}, status= status.HTTP_404_NOT_FOUND)
        



        






    
    

    
