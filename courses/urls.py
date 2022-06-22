from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/', include('main.urls')),
]
if settings.DEBUG:
    urlpatterns += [
        path('', include('rest_framework.urls'))
    ]
