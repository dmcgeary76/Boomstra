from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('Login.urls')),
    path('family/', include('boomstra.addfamily.urls')),
]
