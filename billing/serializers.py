from rest_framework import serializers
from .models import BillingAddress

class BillingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingAddress
        fields = ['street', 'city', 'state', 'postal_code', 'country']