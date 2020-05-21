from rest_framework import serializers 
from api.models.event_model import Event

class EventSerializer(serializers.ModelSerializer):

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

