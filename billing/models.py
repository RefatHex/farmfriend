from django.db import models
from users.models import UserInfo

class BillingAddress(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
