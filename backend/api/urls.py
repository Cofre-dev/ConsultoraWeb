from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'services', views.ServiceViewSet, basename='service')

urlpatterns = [
    path('', include(router.urls)),
]
