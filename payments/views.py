from rest_framework.viewsets import ModelViewSet
from .models import Payments
from .serializers import PaymentsSerializer
from django_filters.rest_framework import DjangoFilterBackend

class PaymentsViewSet(ModelViewSet):
    """
    ViewSet for managing payments with search and filter.
    """
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payment_method', 'status']

    def get_queryset(self):
        """
        Fetch all payments.
        """
        return Payments.objects.all()
