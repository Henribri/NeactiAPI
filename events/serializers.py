from rest_framework import serializers 
from events.models import Event
 
 
class EventSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Event
        fields = ('id',
                  'title',
                  'subtitle',
                  'date',
                  'time',
                  'address',
                  'act_people',
                  'all_people',
                  'description',
                  'category'
                  )