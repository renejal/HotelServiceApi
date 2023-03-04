from rest_framework import generics
from rest_framework import status
from utils.http_response import HttpResponse
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
        result = Hotel.objects.filter()
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
            return Response({'message':"Hotel succesfully removed"}, status.HTTP_200_OK)
    

