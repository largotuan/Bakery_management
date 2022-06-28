from rest_framework import serializers
from .models import Category, Transaction


class GetAllCategorySerializer(serializers.ModelSerializer):
    # transaction_name = serializers.CharField(source='Transaction.name')

    class Meta:
        model = Category
        fields = ['id', 'name']


class PostCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class GetTransactionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Transaction
        fields = ['name', 'category', 'amount', 'note']


class PostTransactionSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.name')

    class Meta:
        model = Transaction
        fields = ['name', 'category', 'amount', 'note']


