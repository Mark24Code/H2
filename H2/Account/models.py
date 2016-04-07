from django.db import models
from django.contrib.auth.models import Group, User
import  mongoengine as mongo

#### Mongo DB Test
# class UserProfile(mongo.Document):
#     pass

class UserProfile(models.Model):
    user = models.ForeignKey(User,unique =True)
    avatar = models.URLField()
    signature = models.CharField(max_length = 140)




