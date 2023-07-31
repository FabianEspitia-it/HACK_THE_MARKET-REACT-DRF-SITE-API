from datetime import datetime



from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status


from baseDB.models import User, ShoppingCart
from .serializer import UserSerializer, RegisterUserSerializer, LoginUserSerializer

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
                user.updated_at = datetime.now()
                user.set_password(request.data["user_password"])
                user.save()
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
            
class RegisterUserAPIView(APIView):
      
      def post(self, request):
            serializer = RegisterUserSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            new_user = User.objects.get(user_email = request.data["user_email"])
            new_user.set_password(request.data["user_password"])
            new_user.is_active= 1
            new_user.created_at = datetime.now()
            new_user.updated_at = datetime.now()
            new_user.save()
            ShoppingCart.objects.create(cart_user = new_user)
            return Response({'message': 'User created succesfully'}, status=status.HTTP_201_CREATED)
            
                 
class LoginUserAPIview(APIView):
     
     def post(self,request):
        try:
            user = User.objects.get(user_email = request.data["user_email"]) 
            if user.check_password(request.data["user_password"]):
                serializer = LoginUserSerializer(data = request.data)
                serializer.is_valid(raise_exception=True)
                return Response({"message": f"Hello, {user.user_name}"}, status=status.HTTP_202_ACCEPTED)
            return Response({"error": "incorrect password"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

          

            
        




