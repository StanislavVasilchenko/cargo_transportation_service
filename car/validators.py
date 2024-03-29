import re

from rest_framework.exceptions import ValidationError


class CarValidatorMixin:
    def __init__(self, field):
        self.fields = field


class CarNumberValidator(CarValidatorMixin):

    def __call__(self, value):
        number = value.get('number')
        pattern = r'^[1-9][0-9]{3}[A-Z]$'
        if not re.match(pattern, number):
            raise ValidationError('Not a valid car number. Input number type by "1111A"')


class CarLiftingValidator(CarValidatorMixin):
    def __call__(self, value):
        lifting_capacity = value.get('lifting_capacity')
        if lifting_capacity > 1000 or lifting_capacity <= 0:
            raise ValidationError('Lifting capacity must be between 0 and 1000 ')
