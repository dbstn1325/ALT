from django.db import models


# Create your models here.

class Order(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, default='')
    category = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    deadLine = models.IntegerField()
