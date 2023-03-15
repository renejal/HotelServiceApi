from base.models import BaseModel
from bookings.models.booking import Booking
from hotels.models.bedroom import Bedroom
from django.db import models

class Availibility(BaseModel):
    bookings = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)
    bedrooms = models.ForeignKey(Bedroom, on_delete=models.CASCADE)
    entry_date = models.DateField(null = True, blank=True)
    departure_date = models.DateField(null = True, blank=True)
    person_count = models.IntegerField(null=True, blank=True, default=12)

    class Meta:
        verbose_name = 'Availability'
        verbose_name_plural = "Availabilitys"
    
    def __str__(self)-> str:
        return str(self.id)
