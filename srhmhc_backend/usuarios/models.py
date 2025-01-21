from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Campo personalizado para roles
    rol = models.CharField(max_length=50, choices=[
        ('ADMINISTRADOR', 'Administrador'),
        ('COORDINADOR', 'Coordinador'),
        ('DATA_ENTRY', 'Data Entry'),
        ('AGENTE', 'Agente'),
    ], default='AGENTE')

    def __str__(self):
        return f"{self.username} ({self.rol})"