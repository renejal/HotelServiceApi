from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.http_response import HttpResponse
from hotels.serializers.bedroom import BedroomCreateSerializer, BedroomUpdateSerializer
from bookings.models import Guest
from hotels.models.hotel import Hotel
from hotels.models.bedroom import Bedroom
from utils.logger_info import MyLogger
logger = MyLogger.__call__().get_logger()

class BedRoomCreateApiView(generics.CreateAPIView):
   serializer_class = BedroomCreateSerializer
   def post(self, request, *args, **kwargs):
      logger.info(request.data)
      serializer = self.get_serializer(data= request.data)
      if serializer.is_valid():
         serializer.create(serializer.data, hotel_id = kwargs.get("hotel_id"))
      return Response({"message": "Habitaciones creadas de forma correcta"})

class BedRoomUpdateApiView(generics.UpdateAPIView):
   serializer_class = BedroomUpdateSerializer
   queryset = Bedroom.objects.all() 

class BedRoomStateUpdate(APIView):
   def put(self, request, *args, **kwargs):
      bedroom = Bedroom.objects.get(id=kwargs["bedroom_id"])
      if bedroom:
         if bedroom.hotel.id == kwargs["hotel_id"]:
            bedroom.state = False if bedroom.state else True
            bedroom.save()
            status = "habilitado" if bedroom.state else "desabilitado"
            return HttpResponse.Success({"message": f"Bedroom id:{kwargs.get('bedroom_id')} {status}"})
         else:
            return HttpResponse.Success({"message": f"bedroom {kwargs.get('bedroom_id')} no pertenece al hotel con id: {kwargs.get('hotel_id')}"})
      return HttpResponse.Success({"message": f"bedroom {kwargs.get('Bedroom_id')} no encontrado"})



