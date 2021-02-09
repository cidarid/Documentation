from django.urls import path
from .views import thermostat_detail_view, thermostat_list_view

app_name = 'thermostat'
urlpatterns = [
    path('', thermostat_list_view, name="thermostat-list"),
    path('<int:my_id>/', thermostat_detail_view, name="thermostat-detail"),
]
