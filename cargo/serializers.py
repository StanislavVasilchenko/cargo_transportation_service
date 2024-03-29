from rest_framework import serializers

from car.models import Car
from cargo.models import Cargo
from cargo.services import get_distance


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class CargoListSerializer(CargoSerializer):
    cars_info = serializers.SerializerMethodField()

    def get_cars_info(self, obj):
        result = []
        cars = Car.objects.all()
        lat_obj = obj.start_location.latitude
        lon_obj = obj.start_location.longitude
        for car in cars:
            lat_car = car.current_location.latitude
            lon_car = car.current_location.longitude
            miles = get_distance(lat_obj, lon_obj, lat_car, lon_car)
            if miles <= 450:
                result.append({car.number: round(miles, 0)})
        return {'count': len(result), 'cars': result}

    class Meta:
        model = Cargo
        fields = ('weight', 'start_location', 'end_location', 'cars_info')


class CargoDetailSerializer(CargoSerializer):
    cars_list = serializers.SerializerMethodField()

    def get_cars_list(self, obj):
        cars = Car.objects.all()
        lat_obj = obj.start_location.latitude
        lon_obj = obj.start_location.longitude
        cars_list = [
            {"car_number": car.number,
             "distance": round(get_distance(lat_obj, lon_obj,
                                            car.current_location.latitude, car.current_location.longitude), 2)}
            for car in cars]
        return cars_list

    class Meta:
        model = Cargo
        fields = ('start_location', 'end_location', 'weight', 'description', 'cars_list')


class CargoUpdateSerializer(CargoSerializer):
    class Meta:
        model = Cargo
        fields = ('weight', 'description',)
