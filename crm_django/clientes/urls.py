from django.urls import path
from . import views

urlpatterns = [
    # Mapeia /clientes/ para a função 'listar_clientes'
    path('', views.listar_clientes, name='listar_clientes'),
    
    # Mapeia /clientes/novo/ para a função 'cadastrar_cliente'
    path('novo/', views.cadastrar_cliente_web, name='cadastrar_cliente_web'),
    
    # Mapeia /clientes/editar/1/ para a função 'editar_cliente_web'
    path('editar/<int:id>/', views.editar_cliente_web, name='editar_cliente_web'),
    
    # Mapeia /clientes/remover/1/ para a função 'remover_cliente_web'
    path('remover/<int:id>/', views.remover_cliente_web, name='remover_cliente_web'),

]