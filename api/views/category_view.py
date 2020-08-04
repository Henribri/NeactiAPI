from api.models.category_model import Category
from api.serializers.category_serializer import CategorySerializer
from rest_framework import generics
from datetime import datetime 


#-- Specifies the query and the serializer to use
#-- in function of the type of the request for Category

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer