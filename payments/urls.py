from rest_framework.routers import DefaultRouter
from .views import PaymentsViewSet

router = DefaultRouter()
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = router.urls
