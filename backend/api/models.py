from django.db import models

# Create your models here.
class EnergyData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    energy_generated = models.FloatField()
    energy_consumed = models.FloatField()

class SolarPanel(models.Model):
    panel_id = models.CharField(max_length= 50, unique=True)
    last_maintenance_date = models.DateField()
    efficiency = models.FloatField()
    current_output = models.FloatField()

    