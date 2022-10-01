from django.db import models

class Movimentacao(models.Model):
    tipo = models.CharField(max_length=100)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField() 
    
    def __str__(self):
        return self.tipo