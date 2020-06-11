from django.urls import path
from .views import DropView
urlpatterns = [
     path('', DropView.as_view(), name='drop'),
    path('<str:customerToken>/', DropView.as_view(), name='drop_particular'),
]
