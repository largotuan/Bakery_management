from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from money_management.models import Category
from .serializers import GetAllCategorySerializer

# Create your views here.


class GetAllCategoryAPIView(APIView):

    def get(self, request):
        list_category = Category.objects.all()
        mydata = GetAllCategorySerializer(list_category, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)
