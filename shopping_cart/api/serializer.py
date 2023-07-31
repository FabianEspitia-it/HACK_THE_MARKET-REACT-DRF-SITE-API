from rest_framework import serializers

from baseDB.models import ShoppingCart, CartProduct


class CartProductSerializer(serializers.ModelSerializer):
    id_product = serializers.StringRelatedField()

    class Meta:
        model = CartProduct
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'product_name': instance.id_product.product_name,
            'product_brand': instance.id_product.product_brand.brand_name,
            'product_price': instance.id_product.product_price
        }
    

class ShoppingCartSerializer(serializers.ModelSerializer):

    cart_delivery_method = serializers.StringRelatedField()
    cart_user = serializers.StringRelatedField()

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    

    def to_representation(self, instance):
        return {
            "cart_id": instance.cart_id,
            "cart_user": instance.cart_user.user_email,
            "products": CartProductSerializer(CartProduct.objects.filter(id_cart = instance.cart_id), many=True).data,
            "cart_delivery_method": instance.cart_delivery_method.delivery_method_name,
            "cart_delivery_cost": instance.cart_delivery_cost,
            "cart_delivery_discount": instance.cart_delivery_discount,
            "cart_total_cost": instance.cart_total_cost

        }

