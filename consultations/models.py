from django.db import models
from users.models import UserInfo

class Agronomist(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='agronomists/')
    dob = models.DateField()
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    availability = models.BooleanField(default=True)

class ConsultationRequest(models.Model):
    farmer = models.ForeignKey('farmers.Farmer', on_delete=models.CASCADE)
    agronomist = models.ForeignKey(Agronomist, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed')
    ])
    details = models.TextField()
    resolution = models.TextField(null=True, blank=True)
