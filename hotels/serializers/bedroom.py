from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.db import transaction
from hotels.models.bedroom import Bedroom
from hotels.models.hotel import Hotel

class BedroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bedroom 
        fields = '__all__'

class BedroomSerializer(serializers.Serializer):
    base_cost = serializers.FloatField(required=True)
    tax = serializers.FloatField(required=True)
    type = serializers.CharField(required=True)
    location = serializers.CharField(required=True)
    state = serializers.BooleanField(required=False, read_only=True, default=True)
    entry_date = serializers.DateField(required=True)
    departure_date = serializers.DateField(required = True)
    person_count = serializers.IntegerField(required = True)


class BedroomCreateSerializer(serializers.Serializer):
    bedrooms = serializers.ListField(child = BedroomSerializer())

    def create(self, validated_data, hotel_id: dict):
        with transaction.atomic():
            hotel = Hotel.objects.get(id=hotel_id)
            if hotel:
                bedrooms_data = validated_data["bedrooms"]
                bedrooms=[
                    Bedroom(hotel=hotel,**bedroom_data) 
                    for bedroom_data in bedrooms_data]
                Bedroom.objects.bulk_create(bedrooms)
            else:
                raise ValidationError({"message":f"No se ha encontrado un hotel con el id {hotel_id}"})
            return True

class BedroomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bedroom
        fields = "__all__"