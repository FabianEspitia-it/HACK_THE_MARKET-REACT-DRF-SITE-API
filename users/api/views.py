#REST_FRAMEWORK
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from baseDB.models import User, ShoppingCart
from .serializer import UserSerializer, RegisterUserSerializer, LoginUserSerializer


class UserAPIView(APIView):

    user = User.objects.filter(user_id=pk).first()

    def get(self, request, pk=None):
        error_message = {"error": "User does not exists"}
        if user:
            if user.is_active == 1:
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)
        return Response(error_message, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        error_message = {'error': 'Something wrong'}
        succesfully_message = {
            'message': 'The information was updated succesfully'}
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user.updated_at = datetime.now()
            user.set_password(request.data["user_password"])
            user.save()
            return Response(succesfully_message, status=status.HTTP_200_OK)
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        error_message = {'error': 'User does not exits'}
        succesfully_message = {'message': 'User deleted succesfully'}
        if user:
            user.is_active = 0
            user.save()
            return Response(succesfully_message, status=status.HTTP_200_OK)
        return Response(error_message, status=status.HTTP_404_NOT_FOUND)


class RegisterUserAPIView(APIView):
    message = {'message': 'User created succesfully'}

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(message, status=status.HTTP_201_CREATED)


class LoginUserAPIview(APIView):
    error_message = {"error": "Invalid credentials"}

    def post(self, request):
        user = User.objects.filter(
            user_email=request.data["user_email"]).first()
        if user:
            if user.check_password(request.data["user_password"]):
                serializer = LoginUserSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                return Response({"message": f"Hello, {user.user_name}"}, status=status.HTTP_202_ACCEPTED)
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
