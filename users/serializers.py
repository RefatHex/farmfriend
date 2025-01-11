from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import UserInfo, UserSessions

class UserInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserInfo
        fields = ['id','user_id', 'username', 'password', 'is_admin', 'is_farmer', 'is_storage_owner', 'is_rent_owner', 'is_agronomist', 'role_count']

    def validate_password(self, value):
        """
        Hash the password before saving.
        """
        return make_password(value)

class UserSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSessions
        fields = ['login_time', 'logout_time', 'session_duration']
