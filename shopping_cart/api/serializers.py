from rest_framework import serializers

from baseDB.models import ShoppingCart, CartProduct, Product


class CartProductSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = CartProduct
        exclude = ['id']
    
    def to_representation(self, instance):

        product = Product.objects.get(product_id = instance.id_product.product_id)
        return {
                "name": product.product_name,
                "brand": product.product_brand.brand_name,
                "category": product.product_category.category_name,
                "price": product.product_price
            }
       



class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        exclude = ['cart_id', 'cart_user']

    def to_representation(self, instance):
        return {
            "cart_user": instance.cart_user.user_email,
            "products": CartProductSerializer(CartProduct.objects.filter(id_cart = instance.cart_id), many=True).data,
            "delivery_method": instance.cart_delivery_method,
            "delivery_cost": instance.cart_delivery_cost,
            "discount": instance.cart_delivery_discount,
            "total_cost": instance.cart_total_cost
        }

