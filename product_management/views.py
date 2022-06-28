from .models import Product, History
from .serializers import GetProductSerializer, PostProductSerializer, GetHistorySerializer, PostHistorySerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class GetProductAPIView(APIView):

    def get(self, request):
        list_product = Product.objects.all()
        serializer = GetProductSerializer(list_product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class GetHistoryAPIVIew(APIView):
    
    def get(self, request):
        list_history = History.objects.all()
        serializer = GetHistorySerializer(list_history, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_503_SERVICE_UNAVAILABLE)



