from django.db import models
from users.models import UserInfo

class Notifications(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    content = models.TextField() 
    is_read = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
