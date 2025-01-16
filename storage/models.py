from django.db import models
from farmers.models import Crops
from users.models import UserInfo

class StorageOwner(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    no_of_deals = models.BigIntegerField(default=0)
    class Meta:
        ordering = ['name']

class StorageOwnerGigs(models.Model):
    storage_owner = models.ForeignKey(StorageOwner, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='storage_gigs/')
    prefered_crop = models.ForeignKey(Crops, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    class Meta:
        ordering = ['-title']

class StorageDeals(models.Model):
    farmer = models.ForeignKey('farmers.Farmer', on_delete=models.CASCADE)
    storage_owner = models.ForeignKey('StorageOwner', on_delete=models.CASCADE)
    crops_taken_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False) 
    is_ready_for_pickup = models.BooleanField(default=False) 
    class Meta:
        ordering = ['-created_at']
