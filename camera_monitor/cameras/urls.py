from django.urls import path
from . import views

urlpatterns = [
    path('', views.camera_list, name='camera_list'),
    path('camera/<int:pk>/', views.camera_detail, name='camera_detail'),
    path('camera/new/', views.camera_create, name='camera_create'),
    path('camera/<int:pk>/edit/', views.camera_update, name='camera_update'),
    path('camera/<int:pk>/delete/', views.camera_delete, name='camera_delete'),
    path('camera/<int:pk>/video_feed/', views.video_feed, name='video_feed'),
]
