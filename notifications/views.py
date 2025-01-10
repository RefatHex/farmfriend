from rest_framework.viewsets import ModelViewSet
from .models import Notifications
from .serializers import NotificationsSerializer

class NotificationsViewSet(ModelViewSet):
    """
    CRUD operations for notifications.
    """
    serializer_class = NotificationsSerializer

    def get_queryset(self):
        """
        Fetch notifications for the authenticated user.
        """
        return Notifications.objects.all()