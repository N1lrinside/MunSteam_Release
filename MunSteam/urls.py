from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('my/admin/', admin.site.urls),
    path('statistic/', include('statistic_from_user.urls')),
    path('user/', include('user.urls', namespace='user')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('achievements.urls')),
    path('', include('games.urls'))
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + debug_toolbar_urls()
