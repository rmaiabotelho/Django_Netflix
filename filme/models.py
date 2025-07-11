from django.db import models
from django.utils import timezone

# Create your models here.
LISTA_CATEGORIA = (
    ('ANALISE', 'Análise'),
    ('PROGRAMAÇÃO', 'Programação'),
    ('APRESENTAÇÃO', 'Apresentação'),
    ('OUTROS', 'Outros')
)
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes/')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIA)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo