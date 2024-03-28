from django.urls import path

from cargo.apps import CargoConfig
from cargo.views import CargoCreateAPIView, CargoListAPIView

app_name = CargoConfig.name

urlpatterns = [
    path('create/', CargoCreateAPIView.as_view(), name='cargo-create'),
    path('list/', CargoListAPIView.as_view(), name='cargo-list'),
]
