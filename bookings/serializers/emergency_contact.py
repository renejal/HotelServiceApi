from rest_framework import serializers
from bookings.models import EmergencyContac
class EmergencyContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmergencyContac
        # fields = "__all__"
        exclude = ("booking",)

