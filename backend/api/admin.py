from django.contrib import admin
from .models import EnergyData, SolarPanel

admin.site.register(EnergyData)
admin.site.register(SolarPanel)

# Register your models here.
