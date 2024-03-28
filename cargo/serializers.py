from rest_framework import serializers

from car.models import Car
from cargo.models import Cargo
from cargo.services import get_distance


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class CargoListSerializer(CargoSerializer):
    cars = serializers.SerializerMethodField()

    def get_cars(self, obj):
        result = []
        cars = Car.objects.all()
        lat_obj = obj.start_location.latitude
        lon_obj = obj.start_location.longitude
        for car in cars:
            lat_car = car.current_location.latitude
            lon_car = car.current_location.longitude
            if get_distance(lat_obj, lon_obj, lat_car, lon_car) <= 450:
                result.append(car)
        return len(result)

    class Meta:
        model = Cargo
        fields = ('start_location', 'end_location', 'cars')

