from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Photo



@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class PhotoListView(View):
    def photo_list_view(request, *args, **kwargs):
        if request.method == 'GET':
            photos = Photo.objects.all()
            photos_data = serialize('json', photos)
            response = HttpResponse(photos_data)
            response['Content-Type'] = 'application/json'
            return response
