from api.models.event_model import Event
from api.serializers.event_serializer import EventSerializer
from rest_framework import generics
from datetime import datetime 
from django.utils import timezone


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects(date_time__gte=timezone.now()).all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

