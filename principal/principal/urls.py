from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    UsuarioViewSet, ClienteViewSet, AdministradorViewSet,
    ContratoViewSet, AtendimentoViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'administradores', AdministradorViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'atendimentos', AtendimentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
