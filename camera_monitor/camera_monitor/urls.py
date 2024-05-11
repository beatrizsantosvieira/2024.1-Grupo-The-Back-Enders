# camera_monitor/urls.py

from django.contrib import admin
from django.urls import path, include  # Importe include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cameras.urls')),  # Inclua as URLs do aplicativo 'cameras'
]
