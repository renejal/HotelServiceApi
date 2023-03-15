from django.db import models
from base.models import BaseModel
from hotels.models.hotel import Hotel

class Bedroom(BaseModel):
    base_cost = models.FloatField(verbose_name="base_cost", blank=False, null=False)
    tax = models.FloatField(verbose_name="tax", blank=True, null=True)
    type = models.CharField(verbose_name="type",max_length=50, blank=False, null=False)
    location = models.CharField(verbose_name="location",max_length=30, blank=False, null=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bedrooms', default=-1)
    person_count = models.IntegerField(null=True, blank=True, default=12)
    

    class Meta:
        verbose_name = 'bedroom'
        verbose_name_plural = "bedrooms"
    
    def __str__(self)-> str:
        return str(self.id)