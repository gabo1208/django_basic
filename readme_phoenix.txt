Grupo Phoenix

Gabriel Freites 08-10383
Edgar Valderrama 09-10870
Sergio Medina 09-11259
Salvador González 10-10296
Valentina Hernández 10-10352
Sergio Barrios 11-10088
Virginia Gil 11-10371
Manuel González 11-10390
Ricardo Munch 11-10684

Para instalar:

- Recomendaciones instalar virtualenv/virtualenvwrapper
* virtualenv: https://virtualenv.pypa.io/en/stable/installation/
* virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/install.html
* Crear env para instalar los requerimientos

- Instalar requirements del requirements.txt con el siguiente comando:
	'$ pip install -r requirements.txt'

- Agregar requerimiento:
* Al instalar alguna libreria nueva para el proyecto ejecutar:
    '$ pip freeze > requirements.txt'
  desde el directorio raiz del repo.

 - Crear usuario:
 	'$ python manage.py createsuperuser'

 - Instalar postgres y crear base de datos llamada django_test
 asi como cambiar la contrasena del usuario "postgres" a "postgres"