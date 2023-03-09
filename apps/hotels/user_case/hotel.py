from utils.http_response import HttpResponse
from hotels.models.hotel import Hotel
class UserCaseHotel:
    def Execute(request):
        Hotel.objects.create()
        return HttpResponse.Success("paso execute")