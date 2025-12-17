from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs do aplicativo clientes. O root / agora leva a 'clientes/'
    path('', include('clientes.urls')), 
]