from rest_framework_mongoengine import serializers 
from api.models.event_model import Event

class GetEventSerializer(serializers.DocumentSerializer):

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
        depth=2

class EventSerializer(serializers.DocumentSerializer):

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

