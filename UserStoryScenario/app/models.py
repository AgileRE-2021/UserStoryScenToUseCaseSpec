# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class project(models.Model):
    id_project = models.AutoField(primary_key=True)
    id_user = models.IntegerField(default=0)
    project_name = models.CharField(max_length=100)
    project_desc = models.TextField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

class feature(models.Model):
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    id_feature = models.AutoField(primary_key=True)
    feature_name = models.CharField(max_length=100)
    feature_action = models.CharField(max_length=100,default='null')
    feature_actor = models.CharField(max_length=100,default='null')
    feature_benefit = models.CharField(max_length=100, default='null')
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

class scenario(models.Model):
    feature = models.ForeignKey(feature, on_delete=models.CASCADE)
    id_scenario = models.AutoField(primary_key=True)
    scenario_name = models.CharField(max_length=100)
    scenario_type = models.CharField(max_length=25)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

class condition(models.Model):
    scenario = models.ForeignKey(scenario, on_delete=models.CASCADE)
    id_condition = models.AutoField(primary_key=True)
    tipe = models.CharField(max_length=25)
    content = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

# Create your models here.

