from base.models import BaseModel
from hotels.models.hotel import Hotel
from hotels.models.bedroom import Bedroom
from django.db import models

class Availibility(BaseModel):
    hotels = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    bedrooms = models.ForeignKey(Bedroom, on_delete=models.CASCADE)
    entry_date = models.DateField(null = True, blank=True)
    departure_date = models.DateField(null = True, blank=True)
    person_count = models.IntegerField(null=True, blank=True, default=12)

    class Meta:
        verbose_name = 'Availability'
        verbose_name_plural = "Availabilitys"
    
    def __str__(self)-> str:
        return str(self.id)
