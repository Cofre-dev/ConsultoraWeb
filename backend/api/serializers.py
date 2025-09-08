# api/serializers.py
from rest_framework import serializers
from core.models import * 

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubmission
        fields = '__all__'
    
    def create(self, validated_data):
        # Obtener IP del request
        request = self.context.get('request')
        if request:
            validated_data['ip_address'] = self.get_client_ip(request)
        
        contact = super().create(validated_data)
        
        # Trigger async tasks
        from .tasks import send_notification_email, sync_to_zoho
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
        fields = '__all__'
        
        
class CarouselSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselSlide
        fields = '__all__'
        
