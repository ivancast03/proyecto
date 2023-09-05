from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



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
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registro/', views.registro, name='registro'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
