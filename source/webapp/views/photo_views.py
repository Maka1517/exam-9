from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from rest_framework.generics import get_object_or_404

from webapp.froms import PhotoForm
from webapp.models import Photo, PhotoLike


class IndexView(ListView):
    model = Photo
    template_name = 'photo/index.html'
    ordering = ['-created_date']
    paginate_by = 5
    context_object_name = 'photos'


class PhotoView(DetailView):
   template_name = 'photo/photo_view.html'
   model = Photo


class PhotoCreatView(LoginRequiredMixin, CreateView):
    template_name = 'photo/photo_create.html'
    model = Photo
    fields = ['picture', 'text']
    # permission_required = 'webapp.add_photo'

    def has_permission(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo/photo_update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'


class PhotoLikeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        liked_photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        like, created = PhotoLike.objects.get_or_create(photo=liked_photo, user=request.user)
        if created:
            liked_photo.save()
            return HttpResponse()
        else:
            return HttpResponseForbidden()


class UnLikeView(LoginRequiredMixin, View):
    def delete(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        like = get_object_or_404(photo.likes, user=request.user)
        like.delete()
        photo.save()
        return HttpResponse()


