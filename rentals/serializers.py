from rest_framework import serializers
from .models import RentOwner, RentItems, RentItemOrders

class RentOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentOwner
        fields = ['user', 'id','name', 'dob', 'contact', 'no_of_deals']

class RentItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentItems
        fields = ['id', 'rent_owner', 'product_name', 'description',"quantity", 'image', 'price', 'is_available']

class RentItemsWithUserSerializer(serializers.ModelSerializer):
    rent_owner=RentOwnerSerializer()
    class Meta:
        model = RentItems
        fields = ['id', 'rent_owner', 'product_name', 'description',"quantity", 'image', 'price', 'is_available']

class RentItemOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentItemOrders
        fields = ['id', 'rent_owner','rent_taker', 'title', 'description', 'image', 'price','order_date','return_date', 'is_confirmed', 'is_ready_for_pickup']
