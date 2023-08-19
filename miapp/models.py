from django.db import models


class Dork(models.Model):
    titulo = models.CharField(max_length=100)
    dork = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
