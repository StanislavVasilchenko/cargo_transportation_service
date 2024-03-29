from django.urls import path

from cargo.apps import CargoConfig
from cargo.views import CargoCreateAPIView, CargoListAPIView, CargoDetailAPIView, CargoUpdateAPIView, \
    CargoDeleteAPIView

app_name = CargoConfig.name

urlpatterns = [
    path('create/', CargoCreateAPIView.as_view(), name='cargo-create'),
    path('list/', CargoListAPIView.as_view(), name='cargo-list'),
    path('detail/<int:pk>/', CargoDetailAPIView.as_view(), name='cargo-detail'),
    path('update/<int:pk>/', CargoUpdateAPIView.as_view(), name='cargo-update'),
    path('delete/<int:pk>/', CargoDeleteAPIView.as_view(), name='cargo-delete'),
]
