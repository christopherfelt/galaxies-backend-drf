from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/galaxies/', include('galaxies.urls')),
    path('api/stars/', include('stars.urls'))
]
