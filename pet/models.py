from django.db import models

# Create your models here.

class Pet(models.Model):
    nome = models.CharField(blank=False, null=False,  max_length=255)
    historia = models.TextField(blank=False, null=False)
    foto = models.URLField(blank=False, null=False)
    