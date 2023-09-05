from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, Group, Permission


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

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    
    # Añade related_name personalizados para evitar conflictos
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_users',  # Cambia 'custom_user_set' a 'custom_users'
        related_query_name='custom_user',
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_users_permissions',  # Cambia 'custom_user_set' a 'custom_users_permissions'
        related_query_name='custom_user_permission',
    )

    def __str__(self):
        return self.username  
