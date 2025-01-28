from django.shortcuts import render
#creating the API for to be able to view the data inside the database 
from rest_framework import viewsets
from .models import EnergyData, SolarPanel
from .serializers import EnergyDataSerializers
from .serializers import SolarPanelDataSerializers


class EnergyDataViewSet(viewsets.ModelViewSet):
    queryset = EnergyData.objects.all()
    serialize_class = EnergyDataSerializers

class SolarPanelViewSet(viewsets.ModelViewSet):
    queryset = SolarPanel.objects.all()
    serializer_class = SolarPanelDataSerializers

