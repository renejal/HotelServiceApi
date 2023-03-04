from django.urls import path
from hotels.views.hotel import HotelListApiView, HotelUpdateView, HotelDeleteView
from bookings.views.guest import GuestListApiView, GuestCreateApiView, GuestDestroyApiView, GuesUpdatApiView



# booking

urlpatterns = [
    path('list', HotelListApiView.as_view(), name='booking list'),
    # path('create', HotelCreateApiView.as_view(), name="booking create" ),
    path('delete', HotelDeleteView.as_view(), name="booking delete"),
    path('update', HotelUpdateView.as_view(), name= "booking update"),
]
#bedrooms


# guest
urlpatterns +=[
    path('guest/list',GuestListApiView.as_view(), name='guest list'),
    path('guest/create', GuestCreateApiView.as_view(), name='guest create'),
    path('guest/update', GuesUpdatApiView.as_view(), name='guest update'),
    path('guest/delete',GuestDestroyApiView.as_view(), name='guest delete'),
]
