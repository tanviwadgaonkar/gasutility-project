from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('customer_service.urls')),  # Include 'customer_service.urls'
    path('', lambda request: redirect('service/')),  # Redirect root to /service/
    path('accounts/', include('django.contrib.auth.urls')),  # Include auth URLs (login, logout, password reset, etc.)
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


