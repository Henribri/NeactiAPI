from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=30, default='Event')
    subtitle=models.CharField(max_length=50, default='No subtitle')
    date=models.DateField(auto_now_add=True)

