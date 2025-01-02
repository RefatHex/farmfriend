from rest_framework.routers import DefaultRouter
from .views import UserInfoViewSet, UserSessionsViewSet

router = DefaultRouter()
router.register(r'user-info', UserInfoViewSet, basename='user-info')
router.register(r'user-sessions', UserSessionsViewSet, basename='user-sessions')

urlpatterns = router.urls
