from rest_framework.routers import DefaultRouter
from .views import BillingAddressViewSet

router = DefaultRouter()
router.register(r'billing-addresses', BillingAddressViewSet, basename='billing-address')

urlpatterns = router.urls
