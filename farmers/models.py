from django.db import models
from users.models import UserInfo

class Farmer(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='farmers/',null=True, blank=True)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    field_size = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    average_rating = models.FloatField(default=0.0)


class FarmerGigs(models.Model):
    farmer = models.ForeignKey('farmers.Farmer', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='farmer_gigs/',null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_at','quantity'] 


class Crops(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='crops/',null=True, blank=True)
