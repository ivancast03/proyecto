# GDYO Generador de Dorks y OSINT

GDYO es un sistema de código abierto diseñado para la prevención de delitos cibernéticos. Permite la generación de Dorks y utiliza técnicas de OSINT (Open Source Intelligence) para recopilar información valiosa en línea. El proyecto está desarrollado en Django y utiliza PostgreSQL como base de datos, Python y Docker para la implementación.

## Instalación
Siga estos pasos para configurar y ejecutar GDYO en su entorno local:
1. Clone el repositorio:
```bash
git clone https://github.com/ivancast03/proyecto
Instale Docker y PostgreSQL, luego cree una base de datos llamada "dork".
Navegue hasta la carpeta del proyecto clonado y cree un entorno virtual:
python -m venv venv
venv\Scripts\activate.bat
Instale las dependencias requeridas:
pip install -r requirements.txt
Realice las migraciones de la base de datos:
python manage.py makemigrations
python manage.py migrate

Inicie el servicio:
python manage.py runserver
El servicio estará disponible localmente en http://127.0.0.1:8000/.

Uso
Generador de Dorks
Ingrese al sistema y seleccione la opción "Generador de Dorks".
El sistema redirigirá a una búsqueda en Google con los dorks generados. Puede personalizarlos según sus necesidades reemplazando "example.com".
Deep Web
Encuentre enlaces onion de ciberdelincuentes y monitórelos en esta sección.
Foros
Explore charlas de hackers y ciberdelincuentes en esta sección.
Ciberseguridad
Acceda a los sitios de ciberseguridad con las últimas noticias en esta sección.
OSINT (Inteligencia de Fuentes Abiertas)
Utilice las herramientas de búsqueda de inteligencia de fuentes abiertas disponibles en esta sección.
Contribución
¡Contribuciones son bienvenidas! Si desea mejorar este proyecto, envíe pull requests o abra problemas.
Licencia
Este proyecto se encuentra bajo la licencia LICENSEGDYO


