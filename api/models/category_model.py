from mongoengine import *

#-- Specifies the type an event

class Category(Document):
    name=StringField(default='Jeux-video', max_length=100)
    iconId=IntField(default=58168)
    fontFamily=StringField(default='MaterialIcons',max_length=100)
    fontPackage=StringField(null=True, max_length=100)
