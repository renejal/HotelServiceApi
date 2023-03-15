from datetime import datetime
from bookings.serializers.availability import AvailabilitySerializer
from rest_framework.views import APIView
from bookings.models.availability import Availibility
from rest_framework.response import Response
from rest_framework.request import Request
from utils.http_response import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class AvailabilityListApiView(APIView):
    "Get bookings"
    serializer_class = AvailabilitySerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('entry_date', openapi.IN_QUERY, description="Fecha de entrada en formato ISO (YYYY-MM-DD)", type=openapi.FORMAT_DATE),
            openapi.Parameter('departure_date', openapi.IN_QUERY, description="Fecha de salida en formato ISO (YYYY-MM-DD)", type=openapi.FORMAT_DATE),
            openapi.Parameter('number_people', openapi.IN_QUERY, description="Cantidad de personas que se alojarán", type=openapi.TYPE_INTEGER),
            openapi.Parameter('destination_city', openapi.IN_QUERY, description="Ciudad donde se crea la reserva", type=openapi.TYPE_STRING),
        ]
    )
    
    def get(self,request:Request, *args, **kwargs):
        entry_date = request.query_params.get("entry_date")
        departure_date = request.query_params.get("departure_date")
        person_count = request.query_params.get("number_people")
        destination_city = request.query_params.get("destination_city")
        if entry_date and departure_date:
            obj_entry_date = datetime.strptime(entry_date, '%Y-%m-%d')
            obj_departure_date = datetime.strptime(departure_date, '%Y-%m-%d')
            if entry_date > departure_date:
                return HttpResponse.Success({"message": "la fecha de ingreso no puede se mayor a la fecha de salida"})
            queryset = Availibility.objects.filter(entry_date__range = (obj_entry_date, obj_departure_date), departure_date__range = (obj_entry_date, obj_departure_date))
            # queryset = Availibility.objects.exclude(entry_date__lt=obj_departure_date, departure_date__gt=obj_entry_date)
        else:
            queryset = Availibility.objects.all()
        return Response({"bookings": AvailabilitySerializer(queryset, many=True).data}) 