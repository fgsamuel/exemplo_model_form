from django.db import models

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=30, unique=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    cor_favorita = models.CharField(max_length=30, blank=True, null=True)
    comida_favorita = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nome
