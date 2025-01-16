from rest_framework.routers import DefaultRouter
from .views import StorageOwnerViewSet, StorageOwnerGigsViewSet, StorageDealsViewSet

router = DefaultRouter()
router.register(r'storage-owners', StorageOwnerViewSet, basename='storage-owners')
router.register(r'storage-gigs', StorageOwnerGigsViewSet, basename='storage-gigs')
router.register(r'storage-deals', StorageDealsViewSet, basename='storage-deals')

urlpatterns = router.urls
