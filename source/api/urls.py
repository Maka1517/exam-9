from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import get_token_view, PhotoListView


router = DefaultRouter()
router.register('photo', PhotoListView, basename='photo')


app_name = 'api'


urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('photos', PhotoListView.as_view(), name='photo_list'),
]