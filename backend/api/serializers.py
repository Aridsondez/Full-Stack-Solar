#creating a searializer to change the database into JSO
from rest_framework import serializers 
from .models import EnergyData, SolarPanel, HouseHold

class SolarPanelDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = SolarPanel
        fields = '__all__'

class EnergyDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = EnergyData
        fields = '__all__'
class HouseHoldDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = HouseHold
        fields = '__all__'
