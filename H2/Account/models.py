from django.db import models
from django.contrib.auth.models import Group, User
import  mongoengine as mongo


class UserProfile(mongo.Document):
    pass


