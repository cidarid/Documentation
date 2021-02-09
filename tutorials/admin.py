from django.contrib import admin
from .models import Tutorial
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')
    search_fields = ['title']


admin.site.register(Tutorial, TutorialAdmin)
