from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path, include
from app.client import urls as client_urls


urlpatterns = [
    path('', include(client_urls)),
    path('admin/', admin.site.urls),
]

AdminSite.site_header = "Gestão de Clientes"
AdminSite.site_title = "Seja bem-vindo"
AdminSite.index_title = "Administração"
