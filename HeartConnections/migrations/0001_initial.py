# Generated by Django 3.2.8 on 2021-12-03 06:55

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('birthdate', models.DateField(default=datetime.date(1900, 1, 1), validators=[django.core.validators.MinValueValidator(datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(datetime.date(2003, 12, 3))])),
                ('gender', models.CharField(max_length=20)),
                ('sexuality', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=40)),
                ('state_region', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('occupation', models.CharField(blank=True, max_length=25, null=True)),
                ('company', models.CharField(blank=True, max_length=40, null=True)),
                ('education', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('religion', models.CharField(blank=True, max_length=25, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=250, null=True)),
                ('dietary_preferences', models.CharField(blank=True, max_length=100, null=True)),
                ('alcohol', models.BooleanField(blank=True, null=True)),
                ('smoking', models.BooleanField(blank=True, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('matched', models.BooleanField(default=False)),
                ('matched_with', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
