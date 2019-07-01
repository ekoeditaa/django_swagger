# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Entity(models.Model):
    model = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
