from django.urls import path
from bookings.views.booking import BookingListApiView, BookingCreateApiView, BookingDestroyApiView, BookingUpdateApiView
from bookings.views.guest import GuestListApiView, GuestCreateApiView, GuestDestroyApiView, GuesUpdatApiView
from bookings.views.availability import AvailabilityListApiView 
# booking
urlpatterns = [
    path('list/', BookingListApiView.as_view(), name='booking list'),
    path('create/', BookingCreateApiView.as_view(), name="booking create" ),
    path('delete/', BookingDestroyApiView.as_view(), name="booking delete"),
    path('update/', BookingUpdateApiView.as_view(), name= "booking update"),
]
#bedrooms
urlpatterns +=[
    path('guest/list/',GuestListApiView.as_view(), name='guest list'),
    path('guest/create/', GuestCreateApiView.as_view(), name='guest create'),
    path('guest/update/', GuesUpdatApiView.as_view(), name='guest update'),
    path('guest/delete/',GuestDestroyApiView.as_view(), name='guest delete'),
]
# availability booking
urlpatterns += [
    path('availability/',AvailabilityListApiView.as_view(), name='availability list'),
]
