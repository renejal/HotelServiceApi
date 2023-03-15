from bookings.serializers.availability import AvailabilitySerializer
from rest_framework.views import APIView
from bookings.models.availability import Availibility
from rest_framework.response import Response

class AvailabilityListApiView(APIView):
    "Get bookings"
    serializer_class = AvailabilitySerializer
    def get(self, *args, **kwargs):
       queryset = Availibility.objects.all()
       return Response({"bookings": AvailabilitySerializer(queryset, many=True).data}) 