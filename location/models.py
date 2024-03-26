from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=100, verbose_name="State")
    zipcode = models.CharField(max_length=100, verbose_name="Zipcode")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    def __str__(self):
        return f'{self.zipcode} - {self.city}'

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ['zipcode']
