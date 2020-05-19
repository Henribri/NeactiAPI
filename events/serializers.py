from rest_framework import serializers 
from events.models import Event


class CategorySerializer(serializers.Serializer):
    _name=serializers.CharField(source='name', default='Sport', max_length=100)
    _iconId=serializers.IntegerField(source='iconId',default=57392)
    _fontFamily=serializers.CharField(source='fontFamily',default='MaterialIcons',max_length=100)
    _fontPackage=serializers.CharField(source='fontPackage', required=False, max_length=100)


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

