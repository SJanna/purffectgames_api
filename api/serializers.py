from .models import Client, Game, Rental
from rest_framework import serializers
from datetime import datetime

    
class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    # client = ClientSerializer()
    games = GameSerializer(many=True, read_only=True)  # Utiliza el serializador GameSerializer

    class Meta:
        model = Rental
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    rental_ids = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = '__all__'


    def get_rental_ids(self, client):
        return client.rentals.values_list('id', flat=True)
    
class CreateRentalSerializer(serializers.Serializer):
    client = ClientSerializer()
    games = serializers.ListField(child=serializers.PrimaryKeyRelatedField(queryset=Game.objects.all()), write_only=True)
    rental_date = serializers.DateTimeField()
    rental_deadline = serializers.DateTimeField()
    price = serializers.FloatField()

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        games_data = validated_data.pop('games')

        client_instance = Client.objects.create(**client_data)

        rental_instance = Rental.objects.create(client=client_instance, **validated_data)
        rental_instance.games.set(games_data)

        # Incrementa el campo rented_times para cada juego en la renta
        for game in games_data:
            game.rented_times += 1
            game.save()

        return rental_instance
    


class AgeRangeSerializer(serializers.Serializer):
    min_age = serializers.IntegerField()
    max_age = serializers.IntegerField()

class MostRentedGameSerializer(serializers.Serializer):
    age_range = AgeRangeSerializer()

    def validate(self, data):
        min_age = data['age_range']['min_age']
        max_age = data['age_range']['max_age']

        if min_age < 0 or max_age < 0:
            raise serializers.ValidationError('Las edades no pueden ser negativas')

        if min_age > max_age:
            raise serializers.ValidationError('La edad mínima no puede ser mayor a la edad máxima')

        return data
    
    def get_most_rented_game(self, min_age, max_age):
        # Calcular las fechas de nacimiento correspondientes a los rangos de edad
        today = datetime.today()
        min_birth_date = today.replace(year=today.year - max_age - 1)
        max_birth_date = today.replace(year=today.year - min_age)

        # Filtrar los clientes dentro del rango de edad y obtener el juego más rentado
        most_rented_game = Game.objects.filter(
            rented_times__gt=0,
            rental__client__birth_date__gte=min_birth_date,
            rental__client__birth_date__lte=max_birth_date
        ).order_by('-rented_times').first()

        return most_rented_game
    
    def to_representation(self, instance):
        most_rented_game = self.get_most_rented_game(
            instance['age_range']['min_age'],
            instance['age_range']['max_age']
        )
        serializer = GameSerializer(most_rented_game)

        return serializer.data