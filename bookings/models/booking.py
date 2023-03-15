from django.db import models
from base.models import BaseModel
from hotels.models.hotel import Hotel

# Create your models here.
class Booking(BaseModel):
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False, blank=False)
    balance_due = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "booking"
        verbose_name_plural = "bookings"

    def __str__(self) -> str:
        return str(super().id)
