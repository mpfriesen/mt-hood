from django.conf.urls import url                                                                                                                              
from django.urls import include, path
from . import views
from .views import image_upload_view, PhotoView

urlpatterns = [ 
    path('', views.default_map, name="default"),
    path('upload/',image_upload_view.as_view(), name='upload'),
    path('photo/', PhotoView.as_view(), name='photo')
 ]