from rest_framework import serializers 
from events.models import Event

 
class CategorySerializer(serializers.Serializer):
    name=serializers.CharField(source='c_name')
    iconId=serializers.IntegerField(source='c_iconId')
    fontFamily=serializers.CharField(source='c_fontFamily')
    fontPackage=serializers.CharField(source='c_fontPackage', required=False)




class EventSerializer(serializers.ModelSerializer):
    category=CategorySerializer(source='*')

    class Meta:
        model = Event
        fields = ('id',
                  'title',
                  'subtitle',
                  'date_time',
                  'address',
                  'act_people',
                  'all_people',
                  'description',
                  'category'
                  )

