from django.urls import path
from .views import DropView
urlpatterns = [
    path('<str:rcNo>/', DropView.as_view(), name='drop'),
]
