from rest_framework import serializers
from bookings.serializers.booking import BookingListSerializer
from hotels.serializers.bedroom import BedroomSerializer

class AvailabilitySerializer(serializers.Serializer):
    entry_date = serializers.DateField()
    departure_date = serializers.DateField()
    person_count = serializers.IntegerField(min_value = 1, max_value = 10, default=2)
    bookings = BookingListSerializer()
    bedrooms = BedroomSerializer() 


    


    


