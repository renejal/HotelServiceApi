from django.db import models
from base.models import BaseModel
from users.models import User
# from hotels.models.bedroom import Bedroom

class Hotel(BaseModel):
    name = models.CharField("name", max_length=50, null=False, unique=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Hotels", blank=True, null=True)
    checkin = models.TimeField(null=True)
    checkout = models.TimeField(null=True)
    destination_city = models.CharField(null=True, max_length=30)

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = "Hotels"

    def __str__(self) -> str:
        return str(self.id)