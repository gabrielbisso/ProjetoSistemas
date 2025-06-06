from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", include('login.urls')),
    path("cadastro/", include('cadastro.urls')),
    path("leitos/", include('leitos.urls')),
]
