from rest_framework.routers import DefaultRouter
from .views import LoginAPIView, UserInfoViewSet, UserSessionsViewSet
from django.urls import path
router = DefaultRouter()
router.register(r'user-info', UserInfoViewSet, basename='user-info')
router.register(r'user-sessions', UserSessionsViewSet, basename='user-sessions')

urlpatterns = router.urls + [
    path('login/', LoginAPIView.as_view(), name='login'),
]
