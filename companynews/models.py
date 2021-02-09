from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=120)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)