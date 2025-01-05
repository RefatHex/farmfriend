from django.contrib import admin
from .models import RentOwner, RentItems, RentItemGigs

@admin.register(RentOwner)
class RentOwnerAdmin(admin.ModelAdmin):
    """
    Admin configuration for RentOwner.
    """
    list_display = ('user', 'name', 'contact', 'no_of_deals')
    search_fields = ('name', 'contact')

@admin.register(RentItems)
class RentItemsAdmin(admin.ModelAdmin):
    """
    Admin configuration for RentItems.
    """
    list_display = ('rent_owner', 'product_name', 'price', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('product_name', 'description')

@admin.register(RentItemGigs)
class RentItemGigsAdmin(admin.ModelAdmin):
    """
    Admin configuration for RentItemGigs.
    """
    list_display = ('rent_owner', 'title', 'price', 'is_confirmed', 'is_ready_for_pickup')
    list_filter = ('is_confirmed', 'is_ready_for_pickup')
    search_fields = ('title', 'description')

    def confirm_gigs(self, request, queryset):
        """
        Custom action to confirm multiple gigs at once.
        """
        queryset.update(is_confirmed=True)
        self.message_user(request, "Selected gigs have been confirmed.")

    confirm_gigs.short_description = "Confirm selected gigs"
    actions = [confirm_gigs]
