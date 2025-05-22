from django.contrib import admin
from .models import Usuario, Cliente, Administrador, Contrato, Atendimento

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Contrato)
admin.site.register(Atendimento)
