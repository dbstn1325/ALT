# Generated by Django 4.1 on 2022-08-06 23:28

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.CharField(max_length=32, null=True)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('page_count', models.IntegerField(default=0)),
                ('email', models.EmailField(error_messages={'unique': 'This email has already been registered.'}, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(default='', error_messages={'unique': 'This phone number has already been registered.'}, max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{3}-\\d{3,4}-\\d{4}$')])),
                ('content', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
