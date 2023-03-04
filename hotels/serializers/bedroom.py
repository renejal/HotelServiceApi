from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.db import transaction
from hotels.models.bedroom import Bedroom
from hotels.models.hotel import Hotel


class BedroomSerializer(serializers.Serializer):
    base_cost = serializers.FloatField(required=True)
    tax = serializers.FloatField(required=True)
    type = serializers.CharField(required=True)
    location = serializers.CharField(required=True)

class BedroomSerializersList(serializers.Serializer):
    bedrooms = serializers.ListField(child = BedroomSerializer())

    def create(self, validated_data, hotel_id: int):
        with transaction.atomic():
            hotel = Hotel.objects.filter(id = hotel_id)
            if hotel:
                bedrooms_data = validated_data["bedrooms"]
                bedrooms=[
                    Bedroom(hotel=hotel,**bedroom_data) 
                    for bedroom_data in bedrooms_data]
                Bedroom.objects.bulk_create(bedrooms)
            else:
                raise ValidationError({"message":f"No se ha encontrado un hotel con el id {hotel_id}"})