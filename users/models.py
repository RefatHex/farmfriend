import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserInfo(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_admin = models.BooleanField(default=False)
    is_farmer = models.BooleanField(default=False)
    is_storage_owner = models.BooleanField(default=False)
    is_rent_owner = models.BooleanField(default=False)
    is_agronomist = models.BooleanField(default=False)
    role_count = models.IntegerField(default=0)


    def save(self, *args, **kwargs):
        # Automatically update role_count based on boolean flags
        self.role_count = sum([self.is_admin, self.is_farmer, self.is_storage_owner, self.is_rent_owner, self.is_agronomist])
        super().save(*args, **kwargs)

class UserSessions(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    session_duration = models.BigIntegerField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
