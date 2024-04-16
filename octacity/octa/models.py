from django.db import models

class Camera(models.Model):
    nome = models.TextField()
    id = models.CharField(max_length=20)

#aqui que o django nos deixa manipular o bd, tipo a criação de uma tabela