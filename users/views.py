from rest_framework.viewsets import ModelViewSet
from .models import UserInfo, UserSessions
from .serializers import UserInfoSerializer, UserSessionsSerializer

class UserInfoViewSet(ModelViewSet):
    """
    CRUD operations for user info.
    """
    serializer_class = UserInfoSerializer

    def get_queryset(self):
        """
        Fetch authenticated user's information.
        """
        return UserInfo.objects.filter(id=self.request.user.id)


class UserSessionsViewSet(ModelViewSet):
    """
    CRUD operations for user sessions.
    """
    serializer_class = UserSessionsSerializer

    def get_queryset(self):
        """
        Fetch sessions for the authenticated user.
        """
        return UserSessions.objects.filter(user=self.request.user)
