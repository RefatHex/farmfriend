from django.db import models

from django.db import models
from users.models import UserInfo
from users.models import UserSessions

class RecAIResponse(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    answer = models.CharField(max_length=255)
    asked_at = models.DateTimeField(auto_now_add=True)
    answer_rating = models.FloatField(null=True, blank=True)
    session_id = models.BigIntegerField()

class FertAIResponse(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()
    crop_type = models.CharField(max_length=255)
    soil_type = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    asked_at = models.DateTimeField(auto_now_add=True)
    answer_rating = models.FloatField(null=True, blank=True)
    session_id = models.BigIntegerField()
