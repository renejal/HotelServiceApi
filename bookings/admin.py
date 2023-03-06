from django.contrib import admin
from bookings.models import Booking, Guest, EmergencyContac

# Register your models here.
admin.site.register(Guest)
admin.site.register(EmergencyContac)
admin.site.register(Booking)
