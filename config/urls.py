from django.contrib import admin
from django.urls import path, include

from config.yasg import swagger_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base_auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/profiles/', include('src.profiles.urls')),
    path('api/heartbeat/', include('src.heartbeat.urls')),
] + swagger_patterns


