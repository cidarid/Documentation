from django.shortcuts import get_object_or_404, render
from .models import Thermostat


# Create your views here.

def thermostat_detail_view(request, my_id):
    obj = get_object_or_404(Thermostat, id=my_id)
    context = {
        'object': obj
    }
    return render(request, "thermostat.html", context)

def thermostat_list_view(request):
    queryset = Thermostat.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "thermostatAll.html", context)
