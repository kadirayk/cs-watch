from django.db import models
from datetime import date

# Create your models here.

class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class Developer(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateField(default=date.today)
    isNobetci = models.BooleanField(default=False)

class Audit(models.Model):
    ip = models.CharField(max_length=20)
    count = models.IntegerField(default=1)
    lastvisit = models.DateTimeField(default=date.today)
