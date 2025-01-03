from django.db import models
from users.models import UserInfo

class RentOwner(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    no_of_deals = models.BigIntegerField(default=0)

class RentItems(models.Model):
    rent_owner = models.ForeignKey(RentOwner, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='rent_items/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

class RentItemGigs(models.Model):
    rent_owner = models.ForeignKey(RentOwner, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='rent_gigs/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
