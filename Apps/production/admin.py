from django.contrib import admin

from .models import *

@admin.register(ProducionDay)
class ProducionDayAdmin(admin.ModelAdmin):
    list_display = ('name_producction','day',)

