from rest_framework import serializers
from .models import RentOwner, RentItems, RentItemGigs

class RentOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentOwner
        fields = ['user', 'name', 'dob', 'contact', 'no_of_deals']

class RentItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentItems
        fields = ['id', 'rent_owner', 'product_name', 'description', 'image', 'price', 'is_available']


class RentItemGigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentItemGigs
        fields = ['id', 'rent_owner', 'title', 'description', 'image', 'price', 'is_confirmed', 'is_ready_for_pickup']
