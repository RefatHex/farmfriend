from rest_framework import serializers
from .models import Payments

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['amount', 'payment_date', 'payment_method', 'status']
