from money_management.models import Category, Transaction
from .serializers import GetAllCategorySerializer, PostCategorySerializer, GetTransactionSerializer, PostTransactionSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# # Create your views here.


class GetAllCategoryAPIView(APIView):

    def get(self, request):
        list_category = Category.objects.all()
        serializer = GetAllCategorySerializer(list_category, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostCategorySerializer(data=request.data)
        if not serializer.is_valid():
            return Response('Sai du lieu roi', status=status.HTTP_401_UNAUTHORIZED)
        catelog_Id = serializer.data['id']
        name = serializer.data['name']

        apipost = Category.objects.create(id=catelog_Id, name=name)
        return Response(data=apipost.category_name, status=status.HTTP_200_OK)


class GetTransactionAPIView(APIView):

    def get(self, request):
        list_transaction = Transaction.objects.all()
        serializer = GetTransactionSerializer(list_transaction, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_503_SERVICE_UNAVAILABLE)

