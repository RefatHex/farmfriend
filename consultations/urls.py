from rest_framework.routers import DefaultRouter
from .views import AgronomistViewSet, ConsultationRequestViewSet

router = DefaultRouter()
router.register(r'agronomists', AgronomistViewSet, basename='agronomist')
router.register(r'consultation-requests', ConsultationRequestViewSet, basename='consultation-request')

urlpatterns = router.urls
