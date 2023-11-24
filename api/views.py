from .models import Client, Game, Rental
from .serializers import ClientSerializer, GameSerializer, RentalSerializer, CreateRentalSerializer, MostRentedGameSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Obtener la lista de IDs de rentas y agregarla al resultado
        rental_ids = instance.rentals.values_list('id', flat=True)
        response_data = serializer.data
        response_data['rental_ids'] = list(rental_ids)

        return Response(response_data)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class ClientRentalsView(generics.ListAPIView):
    serializer_class = RentalSerializer

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        client=Client.objects.get(id=client_id)
        return Rental.objects.filter(client=client)
    

class CreateRentalView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateRentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MostRentedGameByAgeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MostRentedGameSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.data
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)