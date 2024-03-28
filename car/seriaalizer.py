from rest_framework import serializers

from car.models import Car
from car.validators import CarNumberValidator, CarLiftingValidator


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ('current_location',)
        validators = [CarNumberValidator(field='number'),
                      CarLiftingValidator(field='lifting_capacity')]


class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('current_location',)
