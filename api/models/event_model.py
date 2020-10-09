from datetime import datetime 
from django.utils import timezone
from mongoengine import *
from api.models.category_model import Category


#-- Address of event model

class Address(EmbeddedDocument):
    name=StringField()
    lat=FloatField()
    lon=FloatField()
    placeId=StringField()


#-- Event model

class Event(Document):
    title=StringField()
    date_time=DateTimeField()
    address=EmbeddedDocumentField(Address)
    act_people=ListField(StringField(), default=[None])
    all_people=IntField()
    description=StringField()
    category=ReferenceField('Category')
