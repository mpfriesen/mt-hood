from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo

def default_map(request):
    return render(request, 'default.html', {})

class PhotoView(ListView):
    model = Photo
    template_name = 'photo.html'
