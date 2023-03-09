from django.db import models
from base.models import BaseModel, BasePerson
from bookings.models.booking import Booking

class Guest(BasePerson):
    email = models.EmailField()
    phone = models.CharField(verbose_name="phone", max_length=20)
    genero = models.CharField(verbose_name="genero", max_length=10)
    birth_date = models.DateField()
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE,related_name="guests", null=True, blank=True)

    class Meta:
        verbose_name = "Guest"
        verbose_name_plural = "Guests"
    
    def __str__(self) -> str:
        return str(super().id)
