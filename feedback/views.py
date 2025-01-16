from rest_framework.viewsets import ModelViewSet
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class FeedbackViewSet(ModelViewSet):
    """
    ViewSet for managing feedback with search and filter.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['content']
    filterset_fields = ['review_type', 'created_at','user']

    def get_queryset(self):
        """
        Fetch feedback for all users.
        """
        return Feedback.objects.all()
