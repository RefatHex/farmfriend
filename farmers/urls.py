from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet, FarmerGigsViewSet, CropsViewSet

router = DefaultRouter()
router.register(r'farmers', FarmerViewSet, basename='farmer')
router.register(r'farmer-gigs', FarmerGigsViewSet, basename='farmer-gigs')
router.register(r'crops', CropsViewSet, basename='crops')

urlpatterns = router.urls
