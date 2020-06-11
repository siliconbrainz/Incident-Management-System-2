from django.urls import path
from .views import DropCompletedView
urlpatterns = [
     path('', DropCompletedView.as_view(), name='drop_completed'),
    path('<str:customerToken>/', DropCompletedView.as_view(), name='drop_completed_particular'),
]
