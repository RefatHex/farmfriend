from rest_framework.viewsets import ModelViewSet
from .models import StorageOwner, StorageOwnerGigs, StorageDeals
from .serializers import StorageOwnerSerializer, StorageOwnerGigsSerializer, StorageDealsSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StorageOwnerViewSet(ModelViewSet):
    serializer_class = StorageOwnerSerializer

    def get_queryset(self):
        return StorageOwner.objects.filter(user=self.request.user)


class StorageOwnerGigsViewSet(ModelViewSet):
    serializer_class = StorageOwnerGigsSerializer

    def get_queryset(self):
        return StorageOwnerGigs.objects.filter(storage_owner__user=self.request.user)


class StorageDealsViewSet(ModelViewSet):
    """
    ViewSet for managing storage deals with search and filter.
    """
    serializer_class = StorageDealsSerializer
    queryset = StorageDeals.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_confirmed', 'is_ready_for_pickup', 'completed']

    def get_queryset(self):
        """
        Fetch storage deals for the authenticated user.
        """
        user = self.request.user
        return StorageDeals.objects.filter(farmer__user=user) | StorageDeals.objects.filter(storage_owner__user=user)



    def perform_update(self, serializer):
        """
        Handle updates for confirmation and readiness.
        """
        instance = self.get_object()
        if 'is_confirmed' in self.request.data:
            instance.is_confirmed = self.request.data['is_confirmed']
        if 'is_ready_for_pickup' in self.request.data:
            instance.is_ready_for_pickup = self.request.data['is_ready_for_pickup']
        instance.save()
        serializer.save()