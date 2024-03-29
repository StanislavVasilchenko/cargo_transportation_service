from django.db import models

from location.models import Location


class Car(models.Model):
    number = models.CharField(unique=True, max_length=5, verbose_name="car_number")
    current_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, verbose_name="current_location")
    lifting_capacity = models.PositiveIntegerField(verbose_name="lifting_capacity")

    def __str__(self):
        return f"{self.number} - {self.current_location}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['number']
