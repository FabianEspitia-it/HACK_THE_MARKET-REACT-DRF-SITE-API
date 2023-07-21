from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from baseDB.models import User, ShoppingCart
from .serializer import UserSerializer

class UserAPIView(APIView):

    def get(self, request, pk= None):  
            try:
                user = User.objects.get(user_id = pk)
                if user.is_active == 1:
                    serializer = UserSerializer(user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response({'error': 'User does not exits'}, status=status.HTTP_404_NOT_FOUND)
            except:
                 return Response({'error': 'User does not exits'}, status=status.HTTP_404_NOT_FOUND)
                 
    def patch(self, request, pk= None):
            user = User.objects.get(user_id = pk)
            serializer = UserSerializer(user, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'The information was updated succesfully'}, status=status.HTTP_200_OK)
            return Response({'error': 'Something wrong'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk= None):
            try:
                user = User.objects.get(user_id = pk)
                user.is_active = 0
                user.save()
                return Response({'message': 'User deleted succesfully'}, status=status.HTTP_200_OK)
            except:
                 return Response({'error': 'User does not exits'}, status=status.HTTP_404_NOT_FOUND)
            
class CreateUserAPIView(APIView):
      
      def post(self, request):
            serializer = UserSerializer(data = request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                new_user = User.objects.get(user_email = request.data["user_email"])
                ShoppingCart.objects.create(cart_user = new_user)
                return Response({'message': 'User created succesfully'}, status=status.HTTP_201_CREATED)
            return Response({'error': 'Something wrong'}, status=status.HTTP_400_BAD_REQUEST)
                 

            
        




