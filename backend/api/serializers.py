# api/serializers.py
from rest_framework import serializers
from core.models import * 

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'slug', 'short_description', 'description', 'icon', 'is_featured']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'position', 'bio', 'photo', 'linkedin_url', 'is_partner']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = ['full_name', 'email', 'phone', 'company', 'position', 'service_interested', 'message']
    
    def create(self, validated_data):
        # Obtener IP del request
        request = self.context.get('request')
        if request:
            validated_data['ip_address'] = self.get_client_ip(request)
        
        contact = super().create(validated_data)
        
        # Trigger async tasks
        from api.tasks import send_notification_email, sync_to_zoho
        send_notification_email.delay(contact.id)
        sync_to_zoho.delay(contact.id)
        
        return contact
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTestimonial
        fields = ['client_name', 'client_position', 'client_company', 'testimonial', 'rating']