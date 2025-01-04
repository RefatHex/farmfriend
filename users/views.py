from rest_framework.viewsets import ModelViewSet
from .models import UserInfo, UserSessions
from .serializers import UserInfoSerializer, UserSessionsSerializer
from rest_framework.filters import SearchFilter

class UserInfoViewSet(ModelViewSet):
    """
    ViewSet for managing user info with search and filter.
    """
    serializer_class = UserInfoSerializer
    queryset = UserInfo.objects.all()

    filter_backends = [SearchFilter]
    search_fields = ['username', 'email']

    def get_queryset(self):
        """
        Fetch all user profiles.
        """
        return UserInfo.objects.all()



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
