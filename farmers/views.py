from rest_framework.viewsets import ModelViewSet
from .models import Farmer, FarmerGigs, Crops
from .serializers import FarmerSerializer, FarmerGigsSerializer, CropsSerializer

class FarmerViewSet(ModelViewSet):
    """
    CRUD operations for farmers.
    """
    serializer_class = FarmerSerializer

    def get_queryset(self):
        """
        Fetch farmer data for the authenticated user.
        """
        return Farmer.objects.filter(user=self.request.user)


class FarmerGigsViewSet(ModelViewSet):
    """
    CRUD operations for farmer gigs.
    """
    serializer_class = FarmerGigsSerializer

    def get_queryset(self):
        """
        Fetch gigs for the authenticated farmer.
        """
        return FarmerGigs.objects.filter(farmer__user=self.request.user)


class CropsViewSet(ModelViewSet):
    """
    CRUD operations for crops.
    """
    serializer_class = CropsSerializer

    def get_queryset(self):
        """
        Fetch crops for the authenticated farmer.
        """
        return Crops.objects.filter(farmer__user=self.request.user)
