from rest_framework_mongoengine import serializers as mongoserializers
from api.models.event_model import Event, Address
from mongoengine import *


#-- Serialize address of event

class AddressEventSerializer(mongoserializers.EmbeddedDocumentSerializer):

    class Meta:
        model=Address
        fields=(
            'name',
            'lat',
            'lon'
        )



#-- Get the Event and information about its Category

class GetEventSerializer(mongoserializers.DocumentSerializer):
    address=AddressEventSerializer()
    class Meta:
        model = Event
        fields = ('id', 
                   'title',
            #'subtitle',
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
    address=AddressEventSerializer()
    class Meta:
        model = Event
        fields = ('id',
                  'title',
                  #'subtitle',
                  'date_time',
                  'address',
                  'act_people',
                  'all_people',
                  'description',
                  'category'
                  )

