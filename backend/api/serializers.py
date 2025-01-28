#creating a searializer to change the database into JSO
from rest_framework import serializers 
from .models import EnergyData, SolarPanel

class SolarPanelDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = SolarPanel
        fields = '__all__'

class EnergyDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = EnergyData
        fields = '__all__'

