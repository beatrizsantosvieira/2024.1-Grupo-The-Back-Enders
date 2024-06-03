from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('companies/new/', views.company_create, name='company_create'),
    path('companies/<int:pk>/edit/', views.company_update, name='company_update'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),

    path('camera_parks/<int:pk>/', views.camera_park_detail, name='camera_park_detail'),
    path('companies/<int:company_id>/camera_parks/new/', views.camera_park_create, name='camera_park_create'),
    path('camera_parks/<int:pk>/edit/', views.camera_park_update, name='camera_park_update'),
    path('camera_parks/<int:pk>/delete/', views.camera_park_delete, name='camera_park_delete'),

    path('camera/<int:pk>/', views.camera_detail, name='camera_detail'),
    path('camera_parks/<int:camera_park_id>/camera/new/', views.camera_create, name='camera_create'),
    path('camera/<int:pk>/edit/', views.camera_update, name='camera_update'),
    path('camera/<int:pk>/delete/', views.camera_delete, name='camera_delete'),
    path('camera/<int:pk>/video_feed/', views.video_feed, name='video_feed'),
]
