from django.contrib import admin
from bookings.models.emergency_contac import EmergencyContac
from bookings.models.guest import Guest
from bookings.models.booking import Booking
from bookings.models.availability import Availibility

# Register your models here.
admin.site.register(Guest)
admin.site.register(EmergencyContac)
admin.site.register(Booking)
admin.site.register(Availibility)
