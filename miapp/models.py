from django.db import models


class Dork(models.Model):
    titulo = models.CharField(max_length=100)
    dork = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo


class Onion(models.Model):
    pagina = models.CharField(max_length=100)
    onion = models.CharField(max_length=1000)

    def __str__(self):
        return self.pagina  # Devuelve el campo "pagina" en lugar de "titulo"
