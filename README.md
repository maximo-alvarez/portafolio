# portafolio

django admin theme (django interface and django jazzmin django-adminlte-ui)
https://www.youtube.com/watch?v=yA8j-Jn_k8Q
https://django-jazzmin.herokuapp.com/en/admin/
https://django-jazzmin.readthedocs.io/
https://github.com/farridav/django-jazzmin/blob/master/jazzmin/settings.py

import export data
https://python.plainenglish.io/the-easy-way-to-import-export-data-from-django-admin-fe17ecd012fb

github login
https://www.youtube.com/watch?v=RjjEZs4U2Yc
https://github.com/imrohit007/Github-auth-Django
https://medium.com/geekculture/django-social-authentication-sign-in-with-github-33390db1a388

crear archivo cfg.settings.production

copiar contenido de cfg.settings.develop a cfg.settings.production

ingresar los datos de configuración conforme su ambiente de trabajo

python manage.py makemigrations seguridad proyecto

python manage.py migrate

python manage.py createsuperuser

luego de crearse nos presentará un error debido a que no existe el grupo usuario_github mismo que es asignado a 
los usuarios que ingresan por las autenticaciones futuras de github, una vez tengamos acceso al admin debemos crear el 
grupo y asignarles los permisos:

1. Crud completo sobre proyectos
2. Modificar usuario
3. Ver mensajes

Crear las categorías necesarias.