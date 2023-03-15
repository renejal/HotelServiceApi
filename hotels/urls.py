from django.urls import path
from hotels.views.hotel import HotelListApiView, HotelUpdateView, HotelDeleteView, HotelCreateApiView, HotelStateUpdateView
from hotels.views.bedroom import BedRoomCreateApiView, BedRoomUpdateApiView, BedRoomStateUpdate


urlpatterns = [
    path('create/', HotelCreateApiView.as_view(), name='Hotel create'),
    path('list_all/', HotelListApiView.as_view(), name='Hotel'),
    path('update/<int:pk>/', HotelUpdateView.as_view(), name='Hotel update'),
    path('state/<int:hotel_id>/', HotelStateUpdateView.as_view(), name="Hotel State"),
    path('delete/<int:pk>/', HotelDeleteView.as_view(), name='Hotel Delete'),
]
urlpatterns += [
    # path('bedroom/list', BedRoomListApiView.as_view(), name='bedroom list'),
    path('bedroom/create/<int:hotel_id>/', BedRoomCreateApiView.as_view(), name="bedroom create"),
    path('bedroom/update/<int:pk>/', BedRoomUpdateApiView.as_view(), name="bedroom update"),
    path('bedroom/state/<int:hotel_id>/<int:bedroom_id>/', BedRoomStateUpdate.as_view(), name="bedroom state")
    # path('bedroom/delete', BedRoomDestroyApiView.as_view(), name="bedroom delete"),
]




