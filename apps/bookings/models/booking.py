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
