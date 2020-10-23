import pessoas
from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Produto(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_produto = models.CharField(max_length=200)
    detalhes = models.TextField()
    preco = models.CharField(max_length=200)
    date_produto = models.DateTimeField(default=datetime.now, blank=True)
    marca = models.CharField(max_length=200)