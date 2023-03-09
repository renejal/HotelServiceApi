from rest_framework import serializers
from bookings.serializers.emergency_contact import EmergencyContactSerializer
from bookings.serializers.guest import GuestSerializer
from bookings.models.booking import Booking
from hotels.models.hotel import Hotel
from bookings.models.emergency_contac import EmergencyContac
from bookings.models.guest import Guest
from utils.http_response import HttpResponse
from django.db import transaction
from utils.logger_info import MyLogger
logger = MyLogger.__call__().get_logger()

class BookingListSerializer(serializers.ModelSerializer):
    emergency_contacts = EmergencyContactSerializer()
    """ many = true indica que es una relacion de uno a muchos y es espera varios objeto de esta relacion
        read_only = True Indica que es de solo lectura y no se puede modicar en los datos 
    """
    guests = GuestSerializer(many = True, read_only = True) 
    class Meta:
        model = Booking
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    emergency_contacts = EmergencyContactSerializer()
    guests = serializers.ListField(child = GuestSerializer())
    class Meta:
        model = Booking 
        fields = "__all__"

    def create(self, validated_data):
        emergency_contact = validated_data.pop('emergency_contacts')
        with transaction.atomic():
            # en este punto el seralizado ya valdio que el hotel existe, luego trae el objeto hotel en el atributos hotel
            obj_hotel = validated_data.get("hotels")
            logger.debug(obj_hotel)
            if obj_hotel:
                logger.debug("antes de emergencia")
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
                logger.debug("luego de emergencycontact")
                guests_data = validated_data.pop("guests")
                guests = [Guest(booking=obj_booking, **guest_data) for guest_data in guests_data]
                obj_guest=Guest.objects.bulk_create(guests)
                return obj_booking

            logger.error(obj_hotel)
            raise HttpResponse.ServerError("No se encontro hotel") 

    
    