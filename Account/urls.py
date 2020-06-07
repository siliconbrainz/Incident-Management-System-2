
from django.urls import path, include
from .api import UserAPI, LoginAPIAuth #LoginAPI,
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    # path('api/auth/login1', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/login', LoginAPIAuth.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]
