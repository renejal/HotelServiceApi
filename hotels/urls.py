from django.urls import path
from hotels.views.hotel import HotelListApiView, HotelUpdateView, HotelDeleteView, HotelCreateApiView
from hotels.views.bedroom import BedRoomCreateApiView


urlpatterns = [
    path('list_all/', HotelListApiView.as_view(), name='Hotel'),
    path('update/', HotelUpdateView.as_view(), name='Hotel update'),
    path('delete/', HotelDeleteView.as_view(), name='Hotel Delete'),
    path('create/', HotelCreateApiView.as_view(), name='Hotel create'),
    # path('create',create_hotel, name="create_hotel")
]
urlpatterns += [
    # path('bedroom/list', BedRoomListApiView.as_view(), name='bedroom list'),
    path('bedroom/create/<int:hotel_id>', BedRoomCreateApiView.as_view(), name="bedroom create"),
    # path('bedroom/update', BedRoomUpdateApiView.as_view(), name="bedroom update"),
    # path('bedroom/delete', BedRoomDestroyApiView.as_view(), name="bedroom delete"),
]
