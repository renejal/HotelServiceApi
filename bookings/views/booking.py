from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from bookings.serializers.booking import BookingSerializers, BookingListSerializer
from bookings.models import Booking
from users.models import User
from utils.http_response import HttpResponse

# Create your views here.

class BookingListApiView(APIView):
    """Obtener las reservas de un hotel del usuario que se haya logeado"""
    serializer_class=BookingListSerializer # todo elimianr
    def get(self, request, *args, **kwargs):
        queryset = Booking.objects.all() # Todo filter by date
        return Response({"bookings": BookingListSerializer(queryset, many=True).data})


class BookingCreateApiView(generics.CreateAPIView):
    serializer_class = BookingSerializers
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return HttpResponse.Success({"message":"Se creo reserva de forma correcta"})

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

