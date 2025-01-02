from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RecAIResponseView, FertAIResponseView

urlpatterns = [
    path('rec/', RecAIResponseView.as_view(), name='rec-response'),
    path('rec/<int:pk>/', RecAIResponseView.as_view(), name='rec-response-rating'),
    path('fert/', FertAIResponseView.as_view(), name='fert-response'),
    path('fert/<int:pk>/', FertAIResponseView.as_view(), name='fert-response-rating'),
]
