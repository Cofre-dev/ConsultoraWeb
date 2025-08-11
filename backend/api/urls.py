# from django import views
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import *
# from backend.api import views

router = DefaultRouter()

router.register(r'services', ServiceViewSet, basename='service')
router.register(r'team', TestimonialViewSet, basename='teammember')
router.register(r'carousel-slides', CarouselSlideViewSet, basename="carouselslide")

urlpatterns = [
    path('', include(router.urls)),
]

