from django.db import models
from colorfield.fields import ColorField


class Thermostat(models.Model):
    title = models.CharField(max_length=120)
    percent = models.DecimalField(decimal_places=1, max_digits=4, )
    color = ColorField(default='#FF0000')
