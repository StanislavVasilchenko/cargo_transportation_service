import random

from rest_framework import generics, status
from rest_framework.permissions import AllowAny

from car.models import Car
from car.seriaalizer import CarSerializer
from location.models import Location


class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        location = Location.objects.all()[random.randint(1, Location.objects.all().count() - 1)]
        serializer.save(current_location=location)
