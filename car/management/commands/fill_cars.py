import random

from django.core.management import BaseCommand

from car.models import Car
from location.models import Location


class Command(BaseCommand):
    def handle(self, *args, **options):
        cars = []
        count = 1
        location = Location.objects.all()
        for i in range(20):
            car = {
                'number': str(1111 + count) + 'A',
                'current_location': location[random.randint(0, len(location) - 1)],
                'lifting_capacity': 200 + count
            }
            cars.append(Car.objects.create(**car))
            count += 1

        Car.objects.bulk_create(cars)
