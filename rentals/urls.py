from rest_framework.routers import DefaultRouter
from .views import (
    RentOwnerViewSet, 
    RentItemsViewSet, 
    RentItemOrdersViewSet, 
    RentItemsWithUserViewSet
)

router = DefaultRouter()
router.register(r'rent-owners', RentOwnerViewSet, basename='rent-owners')
router.register(r'rent-items', RentItemsViewSet, basename='rent-items')
router.register(r'rent-items-with-user', RentItemsWithUserViewSet, basename='rent-items-with-user')
router.register(r'rent-item-orders', RentItemOrdersViewSet, basename='rent-item-orders')

urlpatterns = router.urls
