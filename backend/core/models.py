from django.db import models
from django.utils import timezone

# Create your models here.
class Service(models.Model):
    #Servicios de Ara y bustamante
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    icon = models.CharField(max_length=50, help_text="Nombre del icono")
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return self.title

class TeamMember(models.Model):
    #Equipo de la consultora
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True)
    linkedin_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_partner = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Miembro del Equipo'
        verbose_name_plural = 'Equipo'
    
    def __str__(self):
        return self.name

class ContactSubmission(models.Model):
    #Formulario de contacto
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('contacted', 'Contactado'),
        ('client', 'Nuevo Cliente'),
        ('rejected', 'No Procede'),
    ]
    
    # Datos del contacto
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=100, blank=True)
    
    # Mensaje
    service_interested = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, help_text="Notas internas")
    
    # Integración
    zoho_lead_id = models.CharField(max_length=100, blank=True)
    synced_to_zoho = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return f"{self.full_name} - {self.company}"

class ClientTestimonial(models.Model):
    #Testimonios de clientes
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)
    testimonial = models.TextField()
    rating = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Testimonio'
        verbose_name_plural = 'Testimonios'
    
    def __str__(self):
        return f"{self.client_name} - {self.client_company}" 