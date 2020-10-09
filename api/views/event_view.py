from api.models.event_model import Event, Category
from api.serializers.event_serializer import GetEventSerializer, EventSerializer
from rest_framework import generics
from datetime import datetime
from django.utils import timezone
from rest_framework import filters


# -- Specifies the query and the serializer to use
# -- in function of the type of the request for Event

# -- General Event List
class EventList(generics.ListCreateAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetEventSerializer
        if self.request.method == 'POST':
            return EventSerializer
        return EventSerializer

    def get_queryset(self):
        queryset = Event.objects(date_time__gte=timezone.now()).all()
        return queryset


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetEventSerializer
        return EventSerializer

    def get_queryset(self):        
        queryset = Event.objects.all()       
        return queryset


# -- List of Events that User have registered
class UserEventList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Event.objects(
            act_people__in=[self.kwargs['userId']], date_time__gte=timezone.now()).all()
        return queryset
    serializer_class = GetEventSerializer


# -- List of Events that User have not registered
class UserNoEventList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Event.objects(act_people__nin=[self.kwargs['userId']], date_time__gte=timezone.now()).aggregate(*[

      {"$lookup": {
                "from": Category._get_collection_name(),  # Tag collection database name
                "foreignField": "_id",  # Primary key of the Tag collection
                "localField": "category",  # Reference field
                "as": "category",
            }}, {"$unwind": "$category"},
            {"$match": {
                "$expr": {"$lt": [{"$size": "$act_people"}, "$all_people"]}}},
                {
      "$addFields":
       {
          "id":"$_id"
       }
  }


        ])


        return queryset

        
    serializer_class = GetEventSerializer
