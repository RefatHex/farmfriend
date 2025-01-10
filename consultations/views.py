from rest_framework.viewsets import ModelViewSet
from .models import Agronomist, ConsultationRequest
from .serializers import AgronomistSerializer, ConsultationRequestSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class AgronomistViewSet(ModelViewSet):
    """
    ViewSet for managing agronomists with search and filter.
    """
    serializer_class = AgronomistSerializer
    queryset = Agronomist.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'specialty']
    filterset_fields = ['availability']

    def get_queryset(self):
        """
        Fetch available agronomists.
        """
        return Agronomist.objects.filter(availability=True)

class ConsultationRequestViewSet(ModelViewSet):
    """
    ViewSet for managing consultation requests with search and filter.
    """
    serializer_class = ConsultationRequestSerializer
    queryset = ConsultationRequest.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'request_date']

    def get_queryset(self):
        """
        Fetch consultation requests for the authenticated farmer.
        """
        return ConsultationRequest.objects.all()
