
from rest_framework_mongoengine import serializers 
from api.models.category_model import Category

#-- Get a Category

class CategorySerializer(serializers.DocumentSerializer):

    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'iconId',
                  'fontFamily',
                  'fontPackage',
                  )

