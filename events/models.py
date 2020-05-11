from django.db import models
from datetime import datetime 


class ActualEvents(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date__gte=datetime.today())



# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=30, default='Event')
    subtitle=models.CharField(max_length=50, default='No subtitle')
    date=models.DateField(default= datetime.date(datetime.now()))
    time=models.TimeField(default= datetime.time(datetime.now()))
    address=models.CharField(max_length=50, default='No address')
    act_people=models.IntegerField(default=0)
    all_people=models.IntegerField(default=0)
    description=models.CharField(max_length=100, default='No description')
    category=models.CharField(max_length=30, default='No category')

    objects = models.Manager()
    actual_events=ActualEvents()