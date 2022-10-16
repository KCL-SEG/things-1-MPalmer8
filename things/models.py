from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model

class Thing(Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField()
    
