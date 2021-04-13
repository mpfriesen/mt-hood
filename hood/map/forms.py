from django import forms
from .models import Photo


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Photo
        fields = ['name', 'email', 'description', 'image']