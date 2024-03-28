import random

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from car.models import Car
from car.seriaalizer import CarSerializer, CarUpdateSerializer
from location.models import Location
from location.services import zip_code_checker


class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        location = Location.objects.all()[random.randint(1, Location.objects.all().count() - 1)]
        serializer.save(current_location=location)


class CarUpdateAPIView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateSerializer
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
        data = request.data
        try:
            location = Location.objects.get(zipcode=zip_code_checker(data['current_location']))
            car = self.get_object()
            car.current_location = location
            car.save()
            return Response(CarUpdateSerializer(car).data, status=status.HTTP_200_OK)
        except Location.DoesNotExist:
            return Response({"message": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
