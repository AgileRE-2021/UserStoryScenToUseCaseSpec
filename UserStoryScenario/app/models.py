# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class project(models.Model):
    id_project = models.AutoField(primary_key=True)
    id_user = models.IntegerField(default=0)
    project_name = models.CharField(max_length=20)
    project_desc = models.TextField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

