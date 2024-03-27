from rest_framework import serializers

from car.models import Car
from car.validators import CarNumberValidator


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('current_location',)
        validators = [CarNumberValidator(field='number'),]
