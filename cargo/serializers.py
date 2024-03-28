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
            if get_distance(lat_obj, lon_obj, car.current_location.latitude, car.current_location.longitude) <= 450:
                result.append(car)
        return len(result)

    class Meta:
        model = Cargo
        fields = ('start_location', 'end_location', 'cars')

