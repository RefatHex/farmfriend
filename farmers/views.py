from rest_framework.viewsets import ModelViewSet
from .models import Farmer, FarmerGigs, Crops
from .serializers import FarmerSerializer, FarmerGigsSerializer, CropsSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class FarmerViewSet(ModelViewSet):
    """
    ViewSet for managing farmers with search and filter.
    """
    serializer_class = FarmerSerializer
    queryset = Farmer.objects.all()

    filter_backends = [SearchFilter]
    search_fields = ['name', 'address']

    def get_queryset(self):
        """
        Fetch farmer profiles.
        """
        return Farmer.objects.all()

class FarmerGigsViewSet(ModelViewSet):
    """
    ViewSet for managing farmer gigs with search and filter.
    """
    serializer_class = FarmerGigsSerializer
    queryset = FarmerGigs.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['farmer', 'is_deleted']

    def get_queryset(self):
        """
        Fetch all gigs, excluding deleted ones.
        """
        return FarmerGigs.objects.filter(is_deleted=False)


class CropsViewSet(ModelViewSet):
    """
    ViewSet for managing crops with search and filter.
    """
    serializer_class = CropsSerializer
    queryset = Crops.objects.all()

    filter_backends = [SearchFilter]
    search_fields = ['name','id']

    def get_queryset(self):
        """
        Fetch crops for all farmers.
        """
        return Crops.objects.all()
