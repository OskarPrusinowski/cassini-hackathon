# Generated by Django 4.2.7 on 2024-09-15 09:50

from django.db import migrations, models
from django.db.models import Model
from django.db.utils import OperationalError

def drop_table_if_exists(apps, schema_editor):
    # Define the table names
    soilprice_table_name = 'SAPP_soilprice'
    soil_table_name = 'SAPP_soil'

    # Drop the 'soilprice' table if it exists
    with schema_editor.connection.cursor() as cursor:
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {soilprice_table_name};")
        except OperationalError:
            pass

        # Drop the 'soil' table if it exists
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {soil_table_name};")
        except OperationalError:
            pass
class Migration(migrations.Migration):

    dependencies = [
        ('SAPP', '0004_seeds_max_t_ha_seeds_min_t_ha_seeds_start_month_and_more'),
    ]

    operations = [
        migrations.RunPython(drop_table_if_exists, reverse_code=migrations.RunPython.noop),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_ph', models.FloatField()),
                ('max_ph', models.FloatField()),
            ],
        ),
    ]