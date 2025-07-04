from django.db import models

# Create your models here.
LISTA_CATEGORIA = (
    ()
)
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='')
    descricao = models.TextField()
    categoraia = models.CharField(max_length=50)
    visualizacoes = 
    data_criacao = 