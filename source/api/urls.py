from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import get_token_view, photo_list_view


router = DefaultRouter()
router.register('photo', photo_list_view, basename='photo')


app_name = 'api'


urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('photos', photo_list_view, name='photo_list'),
]