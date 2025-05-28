from django.db import models
from django.db import models

class Leito(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    ocupado = models.BooleanField(default=False)
    paciente_nome = models.CharField(max_length=100, blank=True, null=True)
    paciente_idade = models.PositiveIntegerField(blank=True, null=True)
    data_internacao = models.DateField(blank=True, null=True)
    motivo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Leito {self.numero} - {'Ocupado' if self.ocupado else 'Livre'}"
