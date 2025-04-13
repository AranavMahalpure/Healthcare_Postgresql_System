from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls_api')),
    path('', include('core.urls_views')),
    path('auth/', include('django.contrib.auth.urls')),
]