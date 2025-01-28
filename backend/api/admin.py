from django.contrib import admin
from .models import EnergyData, HouseHold, SolarPanel

admin.site.register(EnergyData)
admin.site.register(SolarPanel)
admin.site.register(HouseHold)

# Register your models here.
