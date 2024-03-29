from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include([
            path('auth/', include('authentication.urls')),
            path('core/', include('core.urls')),
        ]),
    ),
]
