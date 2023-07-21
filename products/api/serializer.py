from rest_framework import serializers

from baseDB.models import Product



class ProductModelSerializaer(serializers.ModelSerializer):

    product_category = serializers.StringRelatedField()
    product_brand = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'

    
    