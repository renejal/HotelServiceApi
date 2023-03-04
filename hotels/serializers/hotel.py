from hotels.models.hotel import Hotel
from hotels.models.bedroom import Bedroom
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from hotels.serializers.bedroom import BedroomSerializer
from django.db import transaction
from utils.http_response import HttpResponse

class HotelListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=False)
    checkin = serializers.TimeField(required=False)
    checkout = serializers.TimeField(required=False)
    hotel = serializers.PrimaryKeyRelatedField(required=False)
    bedrooms = serializers.ListField(child = BedroomSerializer(), required=False)


class HotelBedroomSerializer(serializers.Serializer):
    bedrooms = serializers.ListField(child = BedroomSerializer() )
    name = serializers.CharField(max_length = 50) 
    checkin = serializers.TimeField(required = True)
    checkout = serializers.TimeField(required = True)
   
    def create(self, validated_data):
        bedrooms_data = validated_data.pop('bedrooms')
        with transaction.atomic():
                print(validated_data)
                hotel = Hotel.objects.filter(name = validated_data["name"])
                if not hotel:
                    hotel = Hotel.objects.create(**validated_data)
                    bedrooms = [Bedroom(hotel=hotel,**bedroom_data) 
                                for bedroom_data in bedrooms_data]
                    Bedroom.objects.bulk_create(bedrooms)
                else:
                    raise ValidationError({"message":f"ya hay un hotel registrado con este nombre: {validated_data['name']}"})
        return hotel 


class HotelSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        exclude = ('create_date','modified_date','deleted_date')

    