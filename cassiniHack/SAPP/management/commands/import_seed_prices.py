import pandas as pd
from django.core.management.base import BaseCommand
from SAPP.models import SeedPrice  # Replace with your actual app name and model

class Command(BaseCommand):
    help = 'Import SeedPrice data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        df = pd.read_csv(csv_file)

        for index, row in df.iterrows():
            seed_id = row['seed_id']
            date = row['date']
            price = row['price']

            # Create or update SeedPrice instance
            SeedPrice.objects.update_or_create(
                # id=1,
                seed_id=seed_id,
                date=date,
                defaults={'price': price}
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported SeedPrice data'))
