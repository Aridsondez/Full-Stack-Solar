from django.db import models

#Recreating the models with households 

class HouseHold(models.Model):
    house_id = models.CharField(max_length= 50, unique=True)
    address = models.CharField(max_length = 255)
    num_solar_panels = models.IntegerField()
    owner_name =models.CharField(max_length =100, blank = True, null= True)

    def __str__(self):
        return f"House {self.house_id} at {self.address}"

class SolarPanel(models.Model):
    panel_id = models.CharField(max_length=50, unique = True)
    household = models.ForeignKey(HouseHold, on_delete=models.CASCADE, related_name="solar_panels", null=True, blank=True)
    last_maintenance_date = models.DateField()
    efficiency = models.FloatField()
    current_output= models.FloatField()

    def __str__(self):
        return f"SolarPanel {self.panel_id} for {self.household.house_id}"


class EnergyData(models.Model):
    household = models.ForeignKey(HouseHold, on_delete= models.CASCADE, related_name= "energy_data", null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add =True)
    energy_generated = models.FloatField()
    energy_consumed = models.FloatField()

    def __str__(self):
        return f"Energy for {self.household.house_id} at {self.timestamp}"

    