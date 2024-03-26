from django.core.management import BaseCommand

from location.models import Location
from location.services import read_csv_locations


class Command(BaseCommand):
    def handle(self, *args, **options):
        locations = read_csv_locations()
        data_for_db = [Location(**location) for location in locations]
        Location.objects.bulk_create(data_for_db)
