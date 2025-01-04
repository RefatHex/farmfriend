from rest_framework import serializers
from .models import StorageOwner, StorageOwnerGigs, StorageDeals

class StorageOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageOwner
        fields = ['name', 'contact', 'no_of_deals']

class StorageOwnerGigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageOwnerGigs
        fields = ['title', 'description', 'price']

class StorageDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageDeals
        fields = ['id', 'farmer', 'storage_owner', 'crops_taken_at', 'created_at', 'completed', 'is_confirmed', 'is_ready_for_pickup']

