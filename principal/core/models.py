from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Cliente(Usuario):
    cpf = models.CharField(max_length=14, unique=True)
    plano_contratado = models.CharField(max_length=100)
    status_pagamento = models.CharField(max_length=50)
    endereco_instalacao = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Administrador(Usuario):
    data_contratacao = models.DateTimeField()
    cargo = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    plano = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

class Atendimento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)
    data_atendimento = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=100)  # ex: técnico, financeiro, etc
    descricao = models.TextField()
    status = models.CharField(max_length=50)  # ex: aberto, em andamento, resolvido

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"
