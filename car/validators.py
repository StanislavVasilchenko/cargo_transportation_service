import re

from rest_framework.exceptions import ValidationError


class CarNumberValidator:
    def __init__(self, field):
        self.fields = field

    def __call__(self, value):
        number = value.get('number')
        pattern = r'^[1-9][0-9]{3}[A-Z]$'
        if not re.match(pattern, number):
            raise ValidationError('Not a valid car number. Input number type by "1111A"')
