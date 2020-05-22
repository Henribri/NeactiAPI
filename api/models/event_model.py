from datetime import datetime 
from django.utils import timezone
from djongo import models





class ActualEvents(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date_time__gte=timezone.now())


class Event(models.Model):
    title=models.CharField(max_length=30, default='Event')
    subtitle=models.CharField(max_length=50, default='No subtitle')
    date_time=models.DateTimeField(default=timezone.now)
    address=models.CharField(max_length=50, default='No address')
    act_people=models.ListField(default=[])
    all_people=models.IntegerField(default=0)
    description=models.CharField(max_length=100, default='No description')
    category=models.IntegerField(default=1)

    objects = models.DjongoManager()
    actual_events=ActualEvents()




