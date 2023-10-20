#DJANGO
from django import datetime


#DJANGO REST FRAMEWORK
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

#DB
from baseDB.models import User, ShoppingCart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginUserSerializer(serializers.Serializer):
    user_email = serializers.CharField(max_length = 100)
    user_password = serializers.CharField(max_length = 200)


class RegisterUserSerializer(serializers.Serializer):
    user_name = serializers.CharField(max_length = 100)
    user_email = serializers.CharField(max_length = 100)
    user_address = serializers.CharField(max_length = 100)
    user_password = serializers.CharField(max_length = 200)
    user_password_confirmation = serializers.CharField(max_length = 200)

    class Meta:
         validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['user_email']
            )
        ]
         
    def validate(self, data):
        if data["user_password"] != data["user_password_confirmation"]:
            raise serializers.ValidationError("Password do not match")
        return data
    
    def create(self, data):
        data.pop("user_password_confirmation")
        data["user_password"] = Users.set_password(data["user_password"])
        user= User.objects.create(**data)
        user.is_active= 1
        user.created_at = datetime.now()
        user.updated_at = datetime.now()
        user.save()
        ShoppingCart.objects.create(cart_user = user)
        return user
        
    