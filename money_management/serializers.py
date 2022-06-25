from rest_framework import serializers
from .models import Category


class GetAllCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
