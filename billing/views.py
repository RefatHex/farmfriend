from rest_framework.viewsets import ModelViewSet
from .models import BillingAddress
from .serializers import BillingAddressSerializer

class BillingAddressViewSet(ModelViewSet):
    """
    CRUD operations for billing addresses.
    """
    serializer_class = BillingAddressSerializer

    def get_queryset(self):
        """
        Fetch billing addresses for the authenticated user.
        """
        return BillingAddress.objects.filter(user=self.request.user)
