import pandas as pd
from django.core.management.base import BaseCommand
from SAPP.models import Seeds  # Replace with your actual app name and model

class Command(BaseCommand):
    help = 'Import Seed data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        df = pd.read_csv(csv_file)

        for index, row in df.iterrows():
            name = row['name']
            min_temp = row['min_temp']
            max_temp = row['max_temp']
            min_rainfall = row['min_rainfall']
            max_rainfall = row['max_rainfall']
            min_ph_soil = row['min_ph_soil']
            max_ph_soil = row['max_ph_soil']

            # Create or update Seed instance
            Seeds.objects.update_or_create(
                name=name,
                defaults={
                    'min_temp': min_temp,
                    'max_temp': max_temp,
                    'min_rainfall': min_rainfall,
                    'max_rainfall': max_rainfall,
                    'min_ph_soil': min_ph_soil,
                    'max_ph_soil': max_ph_soil
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported Seed data'))
