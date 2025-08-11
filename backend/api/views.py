from rest_framework import viewsets, permissions, mixins, status
from rest_framework.response import Response
from core.models import Service, TeamMember, ContactSubmission, ClientTestimonial
from .serializers import ServiceSerializer, TeamMemberSerializer, ContactSerializer, TestimonialSerializer

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver los servicios.
    'ReadOnlyModelViewSet' provee automáticamente las acciones para listar y ver detalles.
    """
    queryset = Service.objects.all().order_by('order')
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny] # Cualquiera puede ver los servicios

class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver los miembros del equipo.
    """
    queryset = TeamMember.objects.all().order_by('order')
    serializer_class = TeamMemberSerializer
    permission_classes = [permissions.AllowAny] # Cualquiera puede ver el equipo

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint que permite ver los testimonios activos.
    """
    queryset = ClientTestimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    permission_classes = [permissions.AllowAny] # Cualquiera puede ver los testimonios

class ContactSubmissionViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint que solo permite la creación (POST) de nuevos envíos de contacto.
    No permite listar, ver detalles, actualizar o borrar contactos desde la API pública.
    """
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny] # Cualquiera puede enviar el formulario

    def create(self, request, *args, **kwargs):
        """
        Sobrescribimos el método create para pasar el 'request' al contexto del serializer.
        Esto es necesario para que el serializer pueda acceder a la IP del cliente.
        """
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Gracias por contactarnos. Nos pondremos en contacto pronto."},
            status=status.HTTP_201_CREATED,
            headers=headers
        )
