from api.models.category_model import Category
from api.serializers.category_serializer import CategorySerializer
from rest_framework import generics
from datetime import datetime 

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer