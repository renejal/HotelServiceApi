from django.contrib import admin
from hotels.models.bedroom import Bedroom
from hotels.models.hotel import Hotel

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Bedroom)