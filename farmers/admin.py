from django.contrib import admin
from .models import Farmer, FarmerGigs, Crops

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    """
    Admin configuration for Farmer.
    """
    list_display = ('user', 'name', 'field_size', 'average_rating')
    list_filter = ('average_rating',)
    search_fields = ('name', 'address')

@admin.register(FarmerGigs)
class FarmerGigsAdmin(admin.ModelAdmin):
    """
    Admin configuration for FarmerGigs.
    """
    list_display = ('farmer', 'title', 'price', 'is_deleted')
    list_filter = ('is_deleted',)
    search_fields = ('title', 'description')

@admin.register(Crops)
class CropsAdmin(admin.ModelAdmin):
    """
    Admin configuration for Crops.
    """
    list_display = ('farmer', 'name')
    search_fields = ('name',)
