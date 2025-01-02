from rest_framework.viewsets import ModelViewSet
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(ModelViewSet):
    """
    CRUD operations for feedback.
    """
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        """
        Fetch feedback for the authenticated user.
        """
        return Feedback.objects.filter(user=self.request.user)
