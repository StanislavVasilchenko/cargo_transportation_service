from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cargo.models import Cargo
from cargo.serializers import CargoSerializer
from location.models import Location
from location.services import zip_code_checker


class CargoCreateAPIView(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            start = Location.objects.get(zipcode=zip_code_checker(request.data['start_location']))
            end = Location.objects.get(zipcode=zip_code_checker(request.data['end_location']))
        except Location.DoesNotExist:
            return Response({'error': 'Invalid zipcode'}, status=status.HTTP_400_BAD_REQUEST)

        new_cargo = Cargo.objects.create(
            start_location=start,
            end_location=end,
            description=request.data.get('description')
        )
        new_cargo.save()
        return Response(CargoSerializer(new_cargo).data, status=status.HTTP_201_CREATED)
