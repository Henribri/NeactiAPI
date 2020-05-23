from datetime import datetime 
from django.utils import timezone
from mongoengine import *
from api.models.category_model import Category




class Event(Document):
    title=StringField(max_length=30, default='Event')
    subtitle=StringField(max_length=50, default='No subtitle')
    date_time=DateTimeField(default=timezone.now)
    address=StringField(max_length=50, default='No address')
    act_people=ListField(StringField(), default=[])
    all_people=IntField(default=0)
    description=StringField(max_length=100, default='No description')
    category=ReferenceField('Category')





