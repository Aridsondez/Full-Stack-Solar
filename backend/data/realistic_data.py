import os
import django 
import random 
import json
from datetime import datetime, timedelta
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "solar_project.settings")

django.setup()

from api.models import HouseHold, EnergyData, SolarPanel

#This is creating a sort of test data that i will be used to vizualize the data 
def create_random_households(num_households = 100):
    house_holds = []

    for i in range(num_households):
        size = random.randint(2517, 5000)
        panels = random.randint(1, 10)

        household = HouseHold.objects.create(
            house_id = f"H{i:03}",
            address = f"{random.randint(1, 6000)}Forest Drive, Orlando FL, 33309",
            num_solar_panels = panels,
            house_size = size,
            owner_name = f" Owner {i}"
        )
        house_holds.append(household)

    return house_holds


def create_solar_panels(households):
    panels = []
    for i in households:
        panel_num = i.num_solar_panels

        for j in range(panel_num):
            
            panel = SolarPanel.objects.create(
                panel_id = f"{i.house_id}_P{j+1}",
                household = i,
                last_maintenance_date = datetime.today() - timedelta(days=random.randint(30, 365)),
                efficiency = random.uniform(80, 100),
                current_output = random.uniform(250, 450)
            )
            panels.append(panel)
    return panels 


WEATHER_CONDITIONS = {
    "Sunny": 1.0,
    "Partly Cloudy": 0.8,
    "Cloudy": 0.6,
    "Rainy" : 0.4,
    "Stormy": 0.2
}

CONSUMPTION_BY_HOUSE_SIZE = {
    "Small": (15, 25),
    "Medium": (25, 40),
    "Large": (40, 60)
}


def create_energy_data(households, days = 365):
    start_date = datetime.today() - timedelta(days = days)

    for day in range(days):
        date = start_date + timedelta(days=day)
        weather = random.choices(list(WEATHER_CONDITIONS.keys()), weights=[50, 20, 15, 10, 5])[0]
        efficiency_factor = WEATHER_CONDITIONS[weather]

        for household in households:
            # Sum up all solar panels' energy generation
            total_generation = sum(
                panel.current_output * efficiency_factor for panel in household.solar_panels.all()
            )

            # Define energy consumption based on house size
            base_consumption_per_sqft = random.uniform(0.015, 0.025) #KWh per square feet
            num_residents = random.randint(2, 5)
            occupancy_factor = (num_residents * random.uniform(1.05, 1.15)) #Energy usage per person on average
            
            total_consumption = household.house_size * base_consumption_per_sqft * occupancy_factor

            # Save energy data record
            EnergyData.objects.create(
                household=household,
                timestamp=date,
                energy_generated=round(total_generation, 2),
                energy_consumed=round(total_consumption, 2)
            )


if __name__ == "__main__":
    print("Generating realistic household energy data...")

    households = create_random_households(100)
    print("Okay households were created ")
    create_solar_panels(households)
    print("Solar Panels were created for each house great")
    create_energy_data(households, days=365)

    print("Database successfully populated with realistic data!")
