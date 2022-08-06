
import datetime
from email.policy import default
from enum import unique
from django.db import models
from django.core.validators import RegexValidator

# Create your models here.



class Order(models.Model):
    design = models.CharField(max_length=32, null=True, blank=False)
    start_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    page_count = models.IntegerField(default=0)
    email = models.EmailField(max_length=254, unique=True, null=True, error_messages={'unique':"This email has already been registered."})
    phoneNumberRegex = RegexValidator(regex = r"^\d{3}-\d{3,4}-\d{4}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, default='', error_messages={'unique':"This phone number has already been registered."})
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
