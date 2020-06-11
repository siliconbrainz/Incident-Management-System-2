
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('Account.urls')),
    path('api/pickup/', include('Pickup.urls')),
    path('api/drop/', include('Drop.urls')),
    path('api/complete/', include('Completed.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
