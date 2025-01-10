from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [ 'user', 'target_user', 'gig_id', 'consultation_id',
            'content', 'rating', 'review_type', 'created_at'
        ]
