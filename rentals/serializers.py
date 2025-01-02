from rest_framework import serializers
from .models import RentOwner, RentItems, RentItemGigs

class RentOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentOwner
        fields = ['name', 'contact', 'no_of_deals']

class RentItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentItems
        fields = ['product_name', 'description', 'price']

class RentItemGigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentItemGigs
        fields = ['title', 'description', 'price']
