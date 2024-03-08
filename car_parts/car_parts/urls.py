from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from part.views import search

urlpatterns = [
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/', search, name='search'),
    path('parts/', include('part.urls')),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)