from rest_framework.viewsets import ModelViewSet
from .models import StorageOwner, StorageOwnerGigs, StorageDeals
from .serializers import StorageOwnerSerializer, StorageOwnerGigsSerializer, StorageDealsSerializer

class StorageOwnerViewSet(ModelViewSet):
    serializer_class = StorageOwnerSerializer

    def get_queryset(self):
        return StorageOwner.objects.filter(user=self.request.user)


class StorageOwnerGigsViewSet(ModelViewSet):
    serializer_class = StorageOwnerGigsSerializer

    def get_queryset(self):
        return StorageOwnerGigs.objects.filter(storage_owner__user=self.request.user)


class StorageDealsViewSet(ModelViewSet):
    serializer_class = StorageDealsSerializer

    def get_queryset(self):
        return StorageDeals.objects.filter(farmer__user=self.request.user)
