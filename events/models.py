from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=30, default='Event')
    subtitle=models.CharField(max_length=50, default='No subtitle')
    date=models.CharField(max_length=10, default='No date')
    time=models.CharField(max_length=10, default='No time')
    address=models.CharField(max_length=50, default='No address')
    act_people=models.IntegerField(default=0)
    all_people=models.IntegerField(default=0)
    description=models.CharField(max_length=100, default='No description')

