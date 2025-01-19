from django.contrib import admin
from .models import StorageOwner, StorageOwnerGigs, StorageDeals

@admin.register(StorageOwner)
class StorageOwnerAdmin(admin.ModelAdmin):
    """
    Admin configuration for StorageOwner.
    """
    list_display = ('user', 'name', 'contact', 'no_of_deals')
    search_fields = ('name', 'contact')

@admin.register(StorageOwnerGigs)
class StorageOwnerGigsAdmin(admin.ModelAdmin):
    """
    Admin configuration for StorageOwnerGigs.
    """
    list_display = ('storage_owner', 'address', 'price')
    search_fields = ('address', 'description')

@admin.register(StorageDeals)
class StorageDealsAdmin(admin.ModelAdmin):
    """
    Admin configuration for StorageDeals.
    """
    list_display = ('farmer', 'storage_owner', 'crops_taken_at', 'completed', 'is_confirmed', 'is_ready_for_pickup')
    list_filter = ('completed', 'is_confirmed', 'is_ready_for_pickup')
    search_fields = ('farmer__user__username', 'storage_owner__user__username')
    date_hierarchy = 'crops_taken_at'
