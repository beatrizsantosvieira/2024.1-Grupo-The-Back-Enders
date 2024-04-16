from django.db import models

class Camera(models.Model):
    nome = models.TextField()
    id = models.CharField(max_length=20)
