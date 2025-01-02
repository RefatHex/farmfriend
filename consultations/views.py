from rest_framework.viewsets import ModelViewSet
from .models import Agronomist, ConsultationRequest
from .serializers import AgronomistSerializer, ConsultationRequestSerializer

class AgronomistViewSet(ModelViewSet):
    """
    CRUD operations for agronomists.
    """
    serializer_class = AgronomistSerializer

    def get_queryset(self):
        """
        Fetch available agronomists.
        """
        return Agronomist.objects.filter(availability=True)


class ConsultationRequestViewSet(ModelViewSet):
    """
    CRUD operations for consultation requests.
    """
    serializer_class = ConsultationRequestSerializer

    def get_queryset(self):
        """
        Fetch consultation requests for the authenticated farmer.
        """
        return ConsultationRequest.objects.filter(farmer__user=self.request.user)
