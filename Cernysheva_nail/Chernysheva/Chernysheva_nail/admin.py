from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Appointment)
admin.site.register(AppointmentChoiceService)
admin.site.register(AppointmentChoiceDateAndTime)
admin.site.register(Promotion)
