
from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status

from events.models import Event
from events.serializers import EventSerializer


@csrf_exempt
def event_list(request):
    if request.method =='GET':
        events=Event.objects.all()
        events_serializer=EventSerializer(events, many=True)
        return JsonResponse(events_serializer.data, safe=False)
    
    elif request.method =='POST':
        event_data=JSONParser().parse(request)
        event_serializer=EventSerializer(data=event_data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse(event_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        event_serializer = EventSerializer(event)
        return JsonResponse(event_serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        event_serializer = EventSerializer(event, data=data)
        if event_serializer.is_valid():
            event_serializer.save()
            return JsonResponse(event_serializer.data)
        return JsonResponse(event_serializer.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)