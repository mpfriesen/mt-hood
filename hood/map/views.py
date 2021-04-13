from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Photo
from .forms import ImageForm

class PhotoView(ListView):
    model = Photo
    template_name = 'photo.html'



class image_upload_view(CreateView):
    """Process images uploaded by users"""
    model = Photo
    form_class=ImageForm
    template_name = 'upload.html'
    success_url = reverse_lazy('photo')

def default_map(request):
    return render(request, 'default.html', {})