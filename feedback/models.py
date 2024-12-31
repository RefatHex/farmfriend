from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE)  
    target_user = models.ForeignKey('users.UserInfo', related_name='reviews_received', on_delete=models.CASCADE, null=True, blank=True)  # Optional target user (e.g., agronomist, rent owner)
    gig_id = models.BigIntegerField(null=True, blank=True) 
    consultation_id = models.BigIntegerField(null=True, blank=True) 
    content = models.TextField()  
    rating = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    REVIEW_TYPE_CHOICES = [
        ('Gig', 'Gig Review'),
        ('Consultation', 'Consultation Feedback'),
        ('General', 'General Feedback'),
    ]
    review_type = models.CharField(max_length=50, choices=REVIEW_TYPE_CHOICES, default='General')
