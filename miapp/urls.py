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
    path("listar_dorks/", views.listar_dorks, name="listar_dorks"),
    path("crear_dork/", views.crear_dork, name="crear_dork"),
    path("editar_dork/<int:pk>/", views.editar_dork, name="editar_dork"),
    path("eliminar_dork/<int:pk>/", views.eliminar_dork, name="eliminar_dork"),
]
