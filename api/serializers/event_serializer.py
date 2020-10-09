from rest_framework_mongoengine import serializers as mongoserializers
from api.models.event_model import Event, Address
from mongoengine import *


# -- Serialize address of event

class AddressEventSerializer(mongoserializers.EmbeddedDocumentSerializer):

    class Meta:
        model = Address
        fields = (
            'name',
            'lat',
            'lon'
        )


# -- Get the Event and information about its Category

class GetEventSerializer(mongoserializers.DocumentSerializer):
    address = AddressEventSerializer()

    class Meta:
        model = Event
        fields = ('id',
                  'title',
                  # 'subtitle',
                  'date_time',
                  'address',
                  'act_people',
                  'all_people',
                  'description',
                  'category'
                  )
        depth = 2


# -- Get the Event without information about its Category (only reference)

class EventSerializer(mongoserializers.DocumentSerializer):
    address = AddressEventSerializer()
    class Meta:
        model = Event
        fields = ('id',
                  'title',
                  # 'subtitle',
                  'date_time',
                  'address',
                  'act_people',
                  'all_people',
                  'description',
                  'category'
                  )

### Check if people clicked in the same time
    def validate_act_people(self, value):
        if (len(value)==len(self.instance["act_people"]) or (len(value)-len(self.instance["act_people"])>1) or (len(self.instance["act_people"])-len(value)>1)):
               raise mongoserializers.me_ValidationError("Click on same time !")
        return value
