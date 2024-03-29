from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cargo.models import Cargo
from cargo.serializers import CargoSerializer, CargoListSerializer, CargoDetailSerializer, CargoUpdateSerializer
from location.models import Location
from location.services import zip_code_checker


class CargoCreateAPIView(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                start = Location.objects.get(zipcode=zip_code_checker(request.data['start_location']))
                end = Location.objects.get(zipcode=zip_code_checker(request.data['end_location']))
            except Location.DoesNotExist:
                return Response({'error': 'Invalid zipcode'}, status=status.HTTP_400_BAD_REQUEST)

            new_cargo = Cargo.objects.create(
                start_location=start,
                end_location=end,
                description=request.data.get('description'),
                weight=request.data.get('weight')
            )
            new_cargo.save()
            return Response(CargoSerializer(new_cargo).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CargoListAPIView(generics.ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoListSerializer
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ({'weight': ['lte']})


class CargoDetailAPIView(generics.RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoDetailSerializer
    permission_classes = [AllowAny]


class CargoUpdateAPIView(generics.UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoUpdateSerializer
    permission_classes = [AllowAny]

    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(
                weight=self.request.data.get('weight'),
                description=self.request.data.get('description')
            )


class CargoDeleteAPIView(generics.DestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [AllowAny]
