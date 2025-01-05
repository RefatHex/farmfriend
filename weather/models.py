from django.db import models

class WeatherUpdate(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.FloatField()
    condition = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Weather in {self.location} - {self.condition}"
