from django.db import models

# Create your models here.

class Storage(models.Model):
    name = models.CharField(max_length=100)
    net = models.BigIntegerField()
    ex = models.IntegerField(null=True)
    sex = models.CharField(max_length=100)
    pet = models.CharField(max_length=100)
    neighbourhood = models.CharField(max_length=100)
