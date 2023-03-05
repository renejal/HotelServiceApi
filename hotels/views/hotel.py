from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from utils.http_response import HttpResponse
from rest_framework.request import Request
from hotels.serializers.hotel import HotelListSerializer, HotelSerializerUpdate, HotelBedroomSerializer 
from hotels.models.hotel import Hotel
from utils.logger_info import MyLogger

logger = MyLogger.__call__().get_logger()

class HotelCreateApiView(generics.CreateAPIView):
    serializer_class = HotelBedroomSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return HttpResponse.Success({"message":"Se creo hotel de forma correcta"})

class HotelListApiView(generics.ListAPIView):
    serializer_class = HotelListSerializer
    def get_queryset(self):
        result = Hotel.objects.filter(state = True)
        return result

class HotelUpdateView(generics.UpdateAPIView):
    serializer_class = HotelSerializerUpdate 
    queryset = Hotel.objects.all()

class HotelDeleteView(generics.DestroyAPIView):
    serializer_class = HotelListSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    def delete(self, request, pk=None):
        hotel = self.get_queryset().filter(id=pk).first()
        if hotel:
            hotel.delete()
            return HttpResponse.Success({'message':"Hotel succesfully removed"})
        return HttpResponse.ServerError({'message':"Hotel no encontrado"})

class HotelStateUpdateView(APIView):
    def put(self, request: Request, *args, **kwargs):
        hotel = Hotel.objects.get(id = kwargs.get("hotel_id"))
        if hotel:
            hotel.state = False if hotel.state else True
            hotel.save()
            status = "habilitado" if hotel.state else "desabilitado"
            return HttpResponse.Success({"message": f"Hotel id:{kwargs.get('hotel_id')} {status}"})
        return HttpResponse.Success({"message": f"hotel {kwargs.get('hotel_id')} no encontrado"})

