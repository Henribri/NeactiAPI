from datetime import datetime 
from django.utils import timezone
from djongo import models



class ActualEvents(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(date_time__gte=timezone.now())


# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=30, default='Event')
    subtitle=models.CharField(max_length=50, default='No subtitle')
    date_time=models.DateTimeField(default=timezone.now)
    address=models.CharField(max_length=50, default='No address')
    act_people=models.IntegerField(default=0)
    all_people=models.IntegerField(default=0)
    description=models.CharField(max_length=100, default='No description')

    #Category
    c_name=models.CharField(default='Sport', max_length=100)
    c_iconId=models.IntegerField(default=57392)
    c_fontFamily=models.CharField(default='MaterialIcons',max_length=100)
    c_fontPackage=models.CharField(null=True, max_length=100)

    objects = models.DjongoManager()
    actual_events=ActualEvents()




