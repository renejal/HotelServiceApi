from rest_framework import generics
from hotels.serializers.bedroom import BedroomSerializersList
from bookings.models import Guest

class BedRoomCreateApiView(generics.CreateAPIView):
   serializer_class = BedroomSerializersList
   def post(self, request, *args, **kwargs):
      serializer = self.get_serializer()
      if serializer.is_valid():
         serializer.save()



