from django.conf.urls import url                                                                                                                              
from django.urls import include, path
from . import views
from .views import PhotoView

urlpatterns = [ 
    path('photos', PhotoView.as_view(), name='photo'),
    url(r'', views.default_map, name="default"),
]