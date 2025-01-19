from rest_framework import serializers
from .models import StorageOwner, StorageOwnerGigs, StorageDeals

class StorageOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageOwner
        fields = ['id','user','name','dob', 'contact', 'no_of_deals']

class StorageOwnerGigsWithDetailsSerializer(serializers.ModelSerializer):
    storage_owner = StorageOwnerSerializer()
    prefered_crop = serializers.StringRelatedField()
    class Meta:
        model = StorageOwnerGigs
        fields = ['storage_owner','address', 'image','description', 'price','is_Available','prefered_crop','quantity']

class StorageDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageDeals
        fields = ['farmer', 'storage_owner', 'crops_taken_at', 'completed', 'is_confirmed', 'is_ready_for_pickup']

class StorageOwnerGigsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageOwnerGigs
        fields = ['storage_owner','address', 'image','description', 'price','is_Available','prefered_crop','quantity']