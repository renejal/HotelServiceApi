from rest_framework import serializers
from bookings.serializers.emergency_contact import EmergencyContactSerializer
from bookings.serializers.guest import GuestSerializer
from bookings.serializers.availability import AvailabilityCreateSerializer
from bookings.models.booking import Booking
from hotels.models.hotel import Hotel
from hotels.models.bedroom import Bedroom
from bookings.models.emergency_contac import EmergencyContac
from bookings.models.guest import Guest
from bookings.models.availability import Availibility
from utils.http_response import HttpResponse
from django.db import transaction
from utils.logger_info import MyLogger
logger = MyLogger.__call__().get_logger()

class BookingListSerializer(serializers.ModelSerializer):
    emergency_contacts = EmergencyContactSerializer()
    """ many = true indica que es una relacion de uno a muchos y es espera varios objeto de esta relacion
        read_only = True Indica que es de solo lectura y no se puede modicar los datos 
    """
    guests = GuestSerializer(many = True, read_only = True) 
    class Meta:
        model = Booking
        fields = '__all__'


class BookingSerializers(serializers.Serializer):
    emergency_contacts = EmergencyContactSerializer()
    guests = serializers.ListField(child = GuestSerializer())
    availability = AvailabilityCreateSerializer()
    bedrooms = serializers.ListField(child=serializers.IntegerField(),
                                     max_length = 5, min_length=1, allow_empty = False)
    hotels = serializers.IntegerField()

    def create(self, validated_data):
        emergency_contact = validated_data.pop('emergency_contacts')
        with transaction.atomic():
            """en este punto el seralizado ya valdio que el hotel existe, luego trae el objeto hotel en el atributos hotel"""
            hotel_id = validated_data.get("hotels")
            obj_availability = validated_data.get("availability")
            bedroom_ids = validated_data.get("bedrooms")
            logger.debug(bedroom_ids)
            obj_hotel = Hotel.objects.get(id=hotel_id)
            if obj_hotel:
                # se buscar el bedroom 
                obj_bedrooms = [obj_hotel.bedrooms.get(id = bedroom_id) for bedroom_id in bedroom_ids ]
                # se crea booking
                obj_booking = Booking.objects.create(hotels=obj_hotel)
                # se agregar a booking contacto de emergencia
                obj_emergency_contact=EmergencyContac.objects.create(
                                               name = emergency_contact["name"],
                                               last_name = emergency_contact["last_name"],
                                               document_number = emergency_contact["document_number"],
                                               document_type = emergency_contact["document_type"],
                                               phone = emergency_contact["phone"],
                                               email = emergency_contact["email"],
                                               booking = obj_booking)
                # se agregar el huesteped a booking
                guests_data = validated_data.pop("guests")
                guests = [Guest(booking=obj_booking, **guest_data) for guest_data in guests_data]
                obj_guest=Guest.objects.bulk_create(guests)
                # se agregan las habitaciones
                if obj_bedrooms:
                    for bedroom in obj_bedrooms:
                        logger.debug(bedroom)
                        Availibility.objects.create(hotels=obj_hotel, 
                                                    bedrooms=bedroom,
                                                    entry_date=obj_availability["entry_date"],
                                                    departure_date=obj_availability["departure_date"])
                return obj_booking

            raise HttpResponse.ServerError("No se encontro hotel") 

    
    