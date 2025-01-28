from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnergyDataViewSet
from .views import SolarPanelViewSet
from .views import HouseHoldViewSet

router = DefaultRouter()
router.register('energy-data', EnergyDataViewSet, basename='energy-data')
router.register('solar-panels', SolarPanelViewSet, basename='solar-panels')
router.register('house-hold', HouseHoldViewSet, basename='house-hold')

urlpatterns = router.urls