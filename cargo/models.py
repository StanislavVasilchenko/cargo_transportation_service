from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from location.models import Location


class Cargo(models.Model):
    start_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='pick_up')
    end_location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='delivery')
    weight = models.FloatField(default=1,
                               validators=[MinValueValidator(1), MaxValueValidator(1000)],
                               verbose_name='weight')

    description = models.TextField(verbose_name='description')

    def __str__(self):
        return (f'description - {self.description}'
                f'start_location - {self.start_location}'
                f'end_location - {self.end_location}'
                f'weight - {self.weight}')

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
        ordering = ['weight']
