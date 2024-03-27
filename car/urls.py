from django.urls import path

from car.apps import CarConfig
from car.views import CarCreateAPIView

app_name = CarConfig.name

urlpatterns = [
    path('create/', CarCreateAPIView.as_view(), name='car-create')
]
