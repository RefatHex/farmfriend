from rest_framework.viewsets import ModelViewSet
from .models import RentOwner, RentItems, RentItemGigs
from .serializers import RentOwnerSerializer, RentItemsSerializer, RentItemGigsSerializer

class RentOwnerViewSet(ModelViewSet):
    serializer_class = RentOwnerSerializer

    def get_queryset(self):
        return RentOwner.objects.filter(user=self.request.user)


class RentItemsViewSet(ModelViewSet):
    serializer_class = RentItemsSerializer

    def get_queryset(self):
        return RentItems.objects.filter(rent_owner__user=self.request.user)


class RentItemGigsViewSet(ModelViewSet):
    serializer_class = RentItemGigsSerializer

    def get_queryset(self):
        return RentItemGigs.objects.filter(rent_owner__user=self.request.user)
