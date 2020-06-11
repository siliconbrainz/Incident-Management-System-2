from django.urls import path
from .views import PickupView
urlpatterns = [
    path('', PickupView.as_view(), name='pickup'),
    path('<str:customerToken>/', PickupView.as_view(), name='pickupSpecific'),
]
