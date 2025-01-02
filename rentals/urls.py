from rest_framework.routers import DefaultRouter
from .views import RentOwnerViewSet, RentItemsViewSet, RentItemGigsViewSet

router = DefaultRouter()
router.register(r'rent-owners', RentOwnerViewSet, basename='rent-owners')
router.register(r'rent-items', RentItemsViewSet, basename='rent-items')
router.register(r'rent-item-gigs', RentItemGigsViewSet, basename='rent-item-gigs')

urlpatterns = router.urls
