# api/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from core.models import ContactSubmission
from .zoho_integration import ZohoIntegration

@shared_task
def send_notification_email(contact_id):
    """Enviar email a secretaria cuando hay nuevo contacto"""
    try:
        contact = ContactSubmission.objects.get(id=contact_id)
        
        subject = f"Nuevo contacto web: {contact.company}"
        message = f"""
        Nuevo contacto desde la web:
        
        Nombre: {contact.full_name}
        Empresa: {contact.company}
        Email: {contact.email}
        Teléfono: {contact.phone}
        Servicio de interés: {contact.service_interested}
        
        Mensaje:
        {contact.message}
        
        ---
        Revisa el panel de administración para más detalles.
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.SECRETARY_EMAIL],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error enviando email: {e}")
        return False

@shared_task
def sync_to_zoho(contact_id):
    """Sincronizar contacto con Zoho CRM"""
    try:
        contact = ContactSubmission.objects.get(id=contact_id)
        zoho = ZohoIntegration()
        
        lead_id = zoho.create_lead({
            'full_name': contact.full_name,
            'company': contact.company,
            'email': contact.email,
            'phone': contact.phone,
            'message': contact.message
        })
        
        if lead_id:
            contact.zoho_lead_id = lead_id
            contact.synced_to_zoho = True
            contact.save()
            return True
    except Exception as e:
        print(f"Error sincronizando con Zoho: {e}")
        return False