from .models import RentOwner, RentItems, RentItemGigs
from .serializers import RentOwnerSerializer, RentItemsSerializer, RentItemGigsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class RentOwnerViewSet(ModelViewSet):
    serializer_class = RentOwnerSerializer

    def get_queryset(self):
        return RentOwner.objects.all()


class RentItemsViewSet(ModelViewSet):
    serializer_class = RentItemsSerializer

    def get_queryset(self):
        return RentItems.objects.all()


class RentItemGigsViewSet(ModelViewSet):
    serializer_class = RentItemGigsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_confirmed', 'is_ready_for_pickup']
    search_fields = ['title', 'description']
    ordering_fields = ['price']

    def get_queryset(self):
        return RentItemGigs.objects.select_related('rent_owner').all()

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