from rest_framework.routers import DefaultRouter
from .views import RentOwnerViewSet, RentItemsViewSet, RentItemOrdersViewSet

router = DefaultRouter()
router.register(r'rent-owners', RentOwnerViewSet, basename='rent-owners')
router.register(r'rent-items', RentItemsViewSet, basename='rent-items')
router.register(r'rent-item-gigs', RentItemOrdersViewSet, basename='rent-item-orders')

urlpatterns = router.urls
