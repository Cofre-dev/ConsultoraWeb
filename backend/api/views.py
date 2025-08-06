from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from django.core.mail import send_mail
from core.models import Service, TeamMember, ContactSubmission, ClientTestimonial
from .serializers import (
    ServiceSerializer, TeamMemberSerializer, 
    ContactSerializer, TestimonialSerializer
)

# Create your views here.

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug' #Todo: Leer que es esto

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured = self.queryset.filter(is_features=True)
        serializer = self.get_serializer(featured, many=True)
        return Response(serializer.data)


class teamViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeamMemberSerializer
    
    def get_queryset(self):
        queryset = TeamMember.objects.all()
        if self.request.query_params.get('partners_only'):
            queryset = queryset.filter(is_partner=True)
        return queryset


class ContactViewSet(viewsets.CreateOnlyModelViewSet):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSerializer
    throttle_classes = [AnonRateThrottle]  # Rate limiting
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {"message": "Gracias por contactarnos. Nos pondremos en contacto pronto."},
            status=status.HTTP_201_CREATED
        )

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ClientTestimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer