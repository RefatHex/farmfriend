from rest_framework.viewsets import ModelViewSet
from .models import UserInfo, UserSessions
from .serializers import UserInfoSerializer, UserSessionsSerializer
from rest_framework.filters import SearchFilter
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo

class LoginAPIView(APIView):
    """
    API View to validate user login.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate input data
        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({
                "user_id": user.user_id,
                "username": user.username,
                "is_admin": user.is_admin,
                "is_farmer": user.is_farmer,
                "is_storage_owner": user.is_storage_owner,
                "is_rent_owner": user.is_rent_owner,
                "is_agronomist": user.is_agronomist,
                "role_count": user.role_count
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

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
