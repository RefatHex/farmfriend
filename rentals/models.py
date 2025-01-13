from django.db import models
from users.models import UserInfo

class RentOwner(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    no_of_deals = models.BigIntegerField(default=0)
    ratings = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        default=0.0  
    )

class RentItems(models.Model):
    rent_owner = models.ForeignKey('RentOwner', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='rent_items/',null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)  

class RentItemOrders(models.Model):
    rent_owner = models.OneToOneField('RentOwner', on_delete=models.CASCADE)
    rent_taker= models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='rent_gigs/',null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False) 
    is_ready_for_pickup = models.BooleanField(default=False) 


