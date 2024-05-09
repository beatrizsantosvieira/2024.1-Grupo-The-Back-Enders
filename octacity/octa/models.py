from django.db import models

class Camera(models.Model):
    nome = models.TextField()
    id = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    data = models.DateTimeField() #tem q ver uma maneira de puxar a data atual
    local = models.TextField()

#aqui que o django nos deixa manipular o bd, como uma criação de tabelas, onde a tabela "Camera" possui as colunas nome e id
