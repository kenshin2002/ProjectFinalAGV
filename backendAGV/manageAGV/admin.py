from django.contrib import admin
from .models import AGV_data,AGV,AGVStates,DataSchedule
# Register your models here.
admin.site.register(AGV_data)
admin.site.register(AGV)
admin.site.register(AGVStates)
admin.site.register(DataSchedule)