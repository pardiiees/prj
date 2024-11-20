from rest_framework import serializers
from shop.models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields= '__all__'

