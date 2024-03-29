import random

from celery import shared_task

from car.models import Car
from location.models import Location


@shared_task
def car_locations_update():
    cars = Car.objects.all()
    locations = Location.objects.all()
    for car in cars:
        car.current_location = locations[random.randint(1, locations.count() - 1)]
        car.save()
