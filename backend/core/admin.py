# core/admin.py
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ['title', 'slug', 'is_featured', 'order']
    list_editable = ['is_featured', 'order']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_partner', 'order']
    list_editable = ['is_partner', 'order']
    list_filter = ['is_partner']

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'company', 'email', 'created_at', 'status', 'synced_to_zoho']
    list_filter = ['status', 'synced_to_zoho', 'created_at']
    search_fields = ['full_name', 'company', 'email']
    readonly_fields = ['created_at', 'ip_address', 'zoho_lead_id']
    
    fieldsets = (
        ('Información de Contacto', {
            'fields': ('full_name', 'email', 'phone', 'company', 'position')
        }),
        ('Mensaje', {
            'fields': ('service_interested', 'message')
        }),
        ('Estado', {
            'fields': ('status', 'notes')
        }),
        ('Metadata', {
            'fields': ('created_at', 'ip_address', 'zoho_lead_id', 'synced_to_zoho'),
            'classes': ('collapse',)
        })
    )
    
    actions = ['mark_as_contacted', 'sync_with_zoho']
    
    def mark_as_contacted(self, request, queryset):
        queryset.update(status='contacted')
    mark_as_contacted.short_description = "Marcar como contactado"
    
    def sync_with_zoho(self, request, queryset):
        from api.tasks import sync_to_zoho
        for contact in queryset:
            sync_to_zoho.delay(contact.id)
    sync_with_zoho.short_description = "Sincronizar con Zoho"

@admin.register(ClientTestimonial)
class ClientTestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_company', 'rating', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active', 'rating']
    

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']