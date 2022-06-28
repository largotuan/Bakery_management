from rest_framework import serializers
from .models import Product, History


class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class PostProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class GetHistorySerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')

    class Meta:
        model = History
        fields = ['product', 'add_action', 'price', 'quantity']

class PostHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = ['product', 'add_action', 'price', 'quantity']
