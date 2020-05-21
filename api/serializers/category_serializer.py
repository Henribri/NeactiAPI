
from rest_framework import serializers 
from api.models.category_model import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'iconId',
                  'fontFamily',
                  'fontPackage',
                  )

