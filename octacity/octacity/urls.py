from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('camera_stream/', views.camera_stream, name='camera_stream'),
]
