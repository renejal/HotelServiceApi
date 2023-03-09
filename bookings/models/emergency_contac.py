from django.db import models
from base.models import BaseModel, BasePerson
from bookings.models.booking import Booking

# Create your models here.
class EmergencyContac(BasePerson):
    booking = models.OneToOneField(Booking,on_delete= models.CASCADE,related_name="emergency_contacts",null=True, blank=True)

    class Meta:
        verbose_name = "Emergency Contac"
        verbose_name_plural = "Emergencies contac"

    def __str__(self) -> str:
        return str(super().id)
    
