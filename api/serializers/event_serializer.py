from rest_framework_mongoengine import serializers as mongoserializers
from api.models.event_model import Event

#-- Get the Event and information about its Category

class GetEventSerializer(mongoserializers.DocumentSerializer):

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


#-- Get the Event without information about its Category (only reference)

class EventSerializer(mongoserializers.DocumentSerializer):

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

