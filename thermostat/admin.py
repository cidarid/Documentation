from django.contrib import admin
from .models import Thermostat


class ThermostatAdmin(admin.ModelAdmin):
    list_display = ('title', 'percent')
    search_fields = ['title']


admin.site.register(Thermostat, ThermostatAdmin)
