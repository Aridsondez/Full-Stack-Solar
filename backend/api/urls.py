from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnergyDataViewSet
from .views import SolarPanelViewSet

router = DefaultRouter()
router.register('energy-data', EnergyDataViewSet, basename='energy-data')
router.register('solar-panels', SolarPanelViewSet, basename='solar-panels')

urlpatterns = router.urls