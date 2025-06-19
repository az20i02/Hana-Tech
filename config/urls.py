from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/home/', include('home.urls')),
    path('api/mission/', include('mission.urls')),
    path('api/services/', include('services.urls')),
    path('api/our-work/', include('our_work.urls')),
    path('api/about/', include('about_us.urls')),
    path('api/core/', include('core.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
