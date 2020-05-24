from api.models.event_model import Event
from api.serializers.event_serializer import GetEventSerializer, EventSerializer
from rest_framework import generics
from datetime import datetime 
from django.utils import timezone



#-- Specifies the query and the serializer to use
#-- in function of the type of the request for Event

class EventList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetEventSerializer
        if self.request.method == 'POST':
            return EventSerializer
        return EventSerializer 
    queryset = Event.objects(date_time__gte=timezone.now()).all()




class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetEventSerializer
        return EventSerializer 
    queryset = Event.objects.all()


