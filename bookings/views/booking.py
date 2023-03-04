from django.shortcuts import render
from bookings.serializers.booking import BookingSerializers
from bookings.models import Booking
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class BookingListApiView(generics.ListAPIView):
    serializer_class = BookingSerializers
    def get_queryset(self):
        result = Booking.objects.filter()
        return result 

class BookingCreateApiView(generics.CreateAPIView):
    serializer_class = BookingSerializers
    queryset = Booking.objects.all()

class BookingDestroyApiView(generics.CreateAPIView):
    def get_queryset(self):
        return self.get_serializer().Meta.model.object.filter(state=True)
    def delete(self, request, pk=None):
        booking = self.get_queryset().filter(id=pk).first()
        if booking:
            booking.delete()
            return Response({'messages':'Booking succesfully removed'})

    serializer_class = BookingSerializers
    queryset = Booking.objects.all()

class BookingUpdateApiView(generics.UpdateAPIView):
    serializer_class = BookingSerializers
    queryset = Booking.objects.all()

