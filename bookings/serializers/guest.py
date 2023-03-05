from rest_framework import serializers
from bookings.models import Guest
class GuestSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()
    # phone = serializers.CharField(max_length=20)
    # genero = serializers.CharField(max_length=10)
    # birth_date = serializers.DateField()
    class Meta:
        model = Guest 
        fields = '__all__'