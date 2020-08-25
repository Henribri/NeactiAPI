from mongoengine import *

#-- Specifies the type an event
class Category(Document):
    name=StringField(max_length=100)
    iconId=IntField()
    fontFamily=StringField(max_length=100)
    fontPackage=StringField(null=True, max_length=100)
