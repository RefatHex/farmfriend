from django.contrib import admin
from .models import Agronomist, ConsultationRequest

@admin.register(Agronomist)
class AgronomistAdmin(admin.ModelAdmin):
    """
    Admin configuration for Agronomist.
    """
    list_display = ('user', 'name', 'specialty', 'years_of_experience', 'availability')
    list_filter = ('specialty', 'availability')
    search_fields = ('name', 'specialty')

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for ConsultationRequest.
    """
    list_display = ('farmer', 'agronomist', 'status', 'request_date', 'details')
    list_filter = ('status', 'request_date')
    search_fields = ('details',)
    date_hierarchy = 'request_date'
