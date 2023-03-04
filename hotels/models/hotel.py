from django.db import models
from base.models import BaseModel
# from hotels.models.bedroom import Bedroom

class Hotel(BaseModel):
    name = models.CharField("name", max_length=50, null=False, unique=True)
    checkin = models.TimeField(null=False)
    checkout = models.TimeField(null=False)
    # bedrooms = models.ForeignKey(Bedroom, on_delete=models.CASCADE, related_name='habitaciones')

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = "Hotels"

    def __str__(self) -> str:
        return self.name