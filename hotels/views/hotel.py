from datetime import datetime
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.http_response import HttpResponse
from rest_framework.request import Request
from hotels.serializers.hotel import HotelListSerializer, HotelSerializerUpdate, HotelBedroomSerializer 
from hotels.models.hotel import Hotel
from utils.logger_info import MyLogger
from datetime import datetime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

logger = MyLogger.__call__().get_logger()

class HotelCreateApiView(generics.CreateAPIView):
    serializer_class = HotelBedroomSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return HttpResponse.Success({"message":"Se creo hotel de forma correcta"})


class HotelListApiView(APIView):
    serializer_class = HotelListSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('entry_date', openapi.IN_QUERY, description="Fecha de entrada en formato ISO (YYYY-MM-DD)", type=openapi.FORMAT_DATE),
            openapi.Parameter('departure_date', openapi.IN_QUERY, description="Fecha de salida en formato ISO (YYYY-MM-DD)", type=openapi.FORMAT_DATE),
            openapi.Parameter('number_people', openapi.IN_QUERY, description="Cantidad de personas que se alojarán", type=openapi.TYPE_INTEGER),
            openapi.Parameter('destination_city', openapi.IN_QUERY, description="Ciudad donde se crea la reserva", type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request: Request, *args, **kwargs):
        entry_date = request.query_params.get("entry_date")
        departure_date = request.query_params.get("departure_date")
        person_count = request.query_params.get("number_people")
        destination_city = request.query_params.get("destination_city")
        if entry_date and departure_date:
            if entry_date > departure_date:
                return HttpResponse.Success({"message": "la fecha de ingreso no puede se mayor a la fecha de salida"})
        queryset = Hotel.objects.filter(bedrooms__state = True).distinct()
        if entry_date and queryset:
            entry_date = datetime.strptime(entry_date,"%Y-%m-%d")
            queryset = queryset.filter(bedrooms__entry_date__gte = entry_date).distinct() # lt > , lte >=
        if departure_date and queryset:
            queryset = queryset.filter(bedrooms__departure_date__lte = departure_date).distinct()
        if person_count and queryset:
            queryset = queryset.filter(bedrooms__person_count__lte = person_count).distinct()
        if queryset and destination_city:
            queryset = queryset.filter(destination_city = destination_city)
        return Response({"hotels": HotelListSerializer(queryset, many=True).data})

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

