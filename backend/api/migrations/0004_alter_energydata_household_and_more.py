# Generated by Django 5.1.5 on 2025-01-28 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_household_energydata_household_solarpanel_household'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energydata',
            name='household',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='energy_data', to='api.household'),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='household',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solar_panels', to='api.household'),
        ),
    ]
