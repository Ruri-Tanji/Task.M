from django.db import models
import datetime
from django.utils import timezone

class Todo(models.Model):
    """Todoリストのモデル"""
    title = models.CharField(max_length=256)
    detail = models.TextField(default='')
    created = models.DateTimeField(default=datetime.datetime.now)
    map = models.CharField(max_length=256)
    now_time = models.DateTimeField(default=timezone.now)

class Memo(models.Model):
    text = models.TextField(default='')
    time = models.DateTimeField(default=timezone.now)