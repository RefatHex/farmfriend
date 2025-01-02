from rest_framework.routers import DefaultRouter
from .views import StorageOwnerViewSet, StorageOwnerGigsViewSet, StorageDealsViewSet

router = DefaultRouter()
router.register(r'storage-owners', StorageOwnerViewSet, basename='storage-owners')
router.register(r'storage-owner-gigs', StorageOwnerGigsViewSet, basename='storage-owner-gigs')
router.register(r'storage-deals', StorageDealsViewSet, basename='storage-deals')

urlpatterns = router.urls
