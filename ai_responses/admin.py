from django.contrib import admin
from .models import RecAIResponse, FertAIResponse

@admin.register(RecAIResponse)
class RecAIResponseAdmin(admin.ModelAdmin):
    """
    Admin configuration for RecAIResponse.
    """
    list_display = ('user', 'nitrogen', 'phosphorus', 'potassium', 'answer', 'asked_at')
    list_filter = ('user', 'asked_at')
    search_fields = ('answer','user',)
    date_hierarchy = 'asked_at'

@admin.register(FertAIResponse)
class FertAIResponseAdmin(admin.ModelAdmin):
    """
    Admin configuration for FertAIResponse.
    """
    list_display = ('user', 'crop_type', 'soil_type', 'answer', 'asked_at')
    list_filter = ('crop_type', 'soil_type', 'asked_at')
    search_fields = ('answer','user',)
    date_hierarchy = 'asked_at'
