from rest_framework import generics
from bookings.models.guest import Guest
from rest_framework.response import Response
from bookings.serializers.guest import GuestSerializer

class GuestListApiView(generics.ListAPIView):
    serializer_class = GuestSerializer 
    def get_queryset(self):
        result = Guest.objects.filter()
        return result

class GuestCreateApiView(generics.CreateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()

class GuestDestroyApiView(generics.DestroyAPIView):
    serializer_class = GuestSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    def delete(self, request, pk=None):
        guest = self.get_queryset().filter(id = pk).first()
        if guest:
            guest.delete()
            return Response({'messages': 'Guest Succesfully remove'})

class GuesUpdatApiView(generics.UpdateAPIView):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()



