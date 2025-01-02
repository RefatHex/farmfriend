from rest_framework.viewsets import ModelViewSet
from .models import Payments
from .serializers import PaymentsSerializer

class PaymentsViewSet(ModelViewSet):
    """
    CRUD operations for payments.
    """
    serializer_class = PaymentsSerializer

    def get_queryset(self):
        """
        Fetch payment records for the authenticated user.
        """
        return Payments.objects.filter(user=self.request.user)
