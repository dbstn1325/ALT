
import datetime
from django.db import models

# Create your models here.



class Order(models.Model):
    design = models.CharField(max_length=32, null=True, blank=False)
    start_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    page_count = models.IntegerField(default=0)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length = 16, default='')
    options = models.CharField(max_length=254, null=True, blank=False)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
