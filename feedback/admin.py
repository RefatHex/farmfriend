from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Admin configuration for Feedback.
    """
    list_display = ('user', 'target_user', 'content', 'rating', 'review_type', 'created_at')
    list_filter = ('review_type', 'rating')
    search_fields = ('content',)
    date_hierarchy = 'created_at'
