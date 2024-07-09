from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include('app.urls')),
    path('', include('beyond_borders.urls')),
    path('', include('community_health_cards.urls')),
    path('', include('home_care_services.urls')),
]