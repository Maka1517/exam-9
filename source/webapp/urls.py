from django.urls import path, include

from webapp.views.photo_views import IndexView, PhotoView, PhotoCreatView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreatView.as_view(), name='photo_create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]