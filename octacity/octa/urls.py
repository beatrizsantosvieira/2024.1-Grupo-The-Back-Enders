from django.urls import path
from . import views

urlpatterns = [
    path('camera_stream/', views.camera_stream, name='camera_stream'),
    path('', views.camera_stream, name='camera_stream'),
]

#esse urls eu apenas copiei da octacity, sendo a urls especifica do app octa