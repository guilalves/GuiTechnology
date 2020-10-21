from django.db import models
from datetime import datetime

class produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    detalhes = models.TextField()
    preco = models.TextField()
    garantia = models.IntegerField()
    date_produto = models.DateTimeField(default=datetime.now, blank=True)