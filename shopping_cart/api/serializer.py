from rest_framework import serializers

from baseDB.models import ShoppingCart, CartProduct


class ShoppingCartSerializer(serializers.ModelSerializer):
    cart_delivery_method = serializers.StringRelatedField()
    cart_user = serializers.StringRelatedField()

    class Meta:
        model = ShoppingCart
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    id_cart = serializers.StringRelatedField()

    class Meta:
        model = CartProduct
        fields = '__all__'