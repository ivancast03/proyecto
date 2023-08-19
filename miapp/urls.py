from django.urls import path
from . import views

urlpatterns = [
    path("", views.mi_vista, name="mi_vista"),  # Usar "mi_vista" como la vista raíz
    path("acerca_de/", views.acerca_de, name="acerca_de"),
    path("soporte/", views.soporte, name="soporte"),
    path(
        "preguntas_frecuentes/", views.preguntas_frecuentes, name="preguntas_frecuentes"
    ),
    path("herramientas/", views.herramientas, name="herramientas"),
]
