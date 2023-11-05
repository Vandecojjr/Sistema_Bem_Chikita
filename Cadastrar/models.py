from django.db import models
from django.contrib.admin.options import ModelAdmin
    
class Materia_prima(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=100)
    u_medida = models.CharField('Un. Medida', max_length=5)
    preco = models.FloatField('Preço', max_length=4)

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.CharField('Descrição', max_length=100)
    preco = models.FloatField('Preço', max_length=4)
    precoAutomatico = models.CharField('precoautomatico', max_length=5)
    porcemPadrao = models.CharField('porcemPadrao', max_length=5)
    porcemLucro = models.IntegerField('%')
    


class Material_do_produto(models.Model):
    idMaterial = models.ForeignKey(Materia_prima, on_delete=models.CASCADE)
    qunat = models.IntegerField('Quantidade')
    idPoduto = models.ForeignKey(Produto, on_delete=models.CASCADE)