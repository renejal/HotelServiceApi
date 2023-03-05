from django.db import models
from base.models import BaseModel, BasePerson
from hotels.models.hotel import Hotel

# Create your models here.
class Booking(BaseModel):
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = "booking"
        verbose_name_plural = "bookings"

    def __str__(self) -> str:
        return str(super().id)
class EmergencyContac(BasePerson):
    booking = models.OneToOneField(Booking,on_delete= models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Emergency Contac"
        verbose_name_plural = "Emergencies contac"

    def __str__(self) -> str:
        return super().name
    
class Guest(BasePerson):
    email = models.EmailField()
    phone = models.CharField(verbose_name="phone", max_length=20)
    genero = models.CharField(verbose_name="genero", max_length=10)
    birth_date = models.DateField()
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"
    
    def __str__(self) -> str:
        return super().name
