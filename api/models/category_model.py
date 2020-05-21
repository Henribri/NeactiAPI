from djongo import models
class Category(models.Model):
    name=models.CharField(default='Sport', max_length=100)
    iconId=models.IntegerField(default=57392)
    fontFamily=models.CharField(default='MaterialIcons',max_length=100)
    fontPackage=models.CharField(null=True, max_length=100)

    objects = models.DjongoManager()