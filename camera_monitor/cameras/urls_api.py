from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CameraViewSet

router = DefaultRouter()
router.register(r'cameras', CameraViewSet)

urlpatterns = [
   path('batata', include(router.urls)), # decidir qual vai ser a rota
]
