from django.db import models

class Conteiner(models.Model):
    nome_cliente = models.CharField(max_length=100)
    num_conteiner = models.CharField(max_length=11)
    tipo_conteiner = models.IntegerField() 
    status_conteiner = models.CharField(max_length=5)
    categoria_conteiner = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome_cliente