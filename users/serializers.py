from rest_framework import serializers
from .models import UserInfo, UserSessions

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user_id', 'is_admin', 'is_farmer', 'is_storage_owner', 'is_rent_owner', 'is_agronomist', 'role_count']

class UserSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSessions
        fields = ['login_time', 'logout_time', 'session_duration']
