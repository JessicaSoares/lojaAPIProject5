from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=140)
    preco = models.CharField(max_length=140)


    class Meta:
        ordering = ['nome']
