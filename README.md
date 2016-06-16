# API RESTFul con REST Framework de Django

Pequeño tutorial sobre como hacer uso de django-restframework, utilizando las clases de serialización de modelos y vistas personalizadas para poder realizar cualquier otro tipo de operación.

## Contenido

A continuación se describe el proceso para poder conseguir un código similar al que se comparte de ejemplo en el presente repositorio.

### Haciendo magia (pip-install)

PIP es una herramienta que nos permitirá contar con todos los paquetes y dependendencias necesarias, en este caso usaremos los siguientes:

```shell
pip install django
pip install djangorestframework
pip install markup
pip install django-filter
pip install django-grappelli
```

### Configurando Django

Ahora debemos realizar la configuración necesaria del settings, para poder usar apropiadamente el paquete de restframework.

* Con el archivo settings.py

```python
INSTALLED_APPS = [
    'grappelli',
    .
    .
    .
    'rest_framework',
    ]

.
.
.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

.
.
.

STATIC_ROOT = 'html/'
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

```

### Creando modelos, funciones y algunas clases

Enseguida procedemos a crear algunos modelos, para completar adecuadamente el ejemplo, así como unas funciones y otras clases, para un servicio personalizado y también para usar los serializadores con los modelos básicos de django Auth.

* En el archivo *models.py* definimos los modelos propios, definir los necesarios en otras 'webapps'

```python
CONTACT_TYPES = (
    ('Emisor', 'Emisor'),
    ('Receptor', 'Receptor'),
)


class Servicio(models.Model):
    nombre = models.CharField(max_length=1024, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    .
    .
    .
```

* Con el archivo *serializers.py* definimos las clases que se van a usar para serializar los modelos que fueron definidos en el archivo anterior.

```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
    .
    .
    .
```

* Con el archivo *urls.py* registramos cada set de vistas serializadas, en el enrutador correspondiente con los nombres que definamos según el uso de cada uno.

```python
.
.
.
class UserViewSet(viewsets.ModelViewSet):
    """
    Servicio API para visualizar o editar a los usuarios del sistema
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    .
    .
    .
```

### CSRF ?? CORS ??

La protección *Cross Site Request Forgery* es un mecanismo de protección contra un tipo particular de ataque, lo que puede ocurrir cuando un usuario no ha cerrado la sesión de un sitio web, y sigue teniendo una sesión válida. En esta circunstancia un sitio malicioso puede ser capaz de realizar acciones contra el sitio de destino, en el contexto de la sesión iniciado la sesión.

Un claro ejemplo de lo anterior, es cuando deshabilitamos el control en nuestro ejemplo (linea 35 urls.py) o intentamos enviar una solicitud a servicio de tipo POST/PUT sin el token correspondiente.

El mecanismo *Cross-Origin Resource Sharing* es un mecanismo para permitir que los clientes interactuen con las API que están alojadas en un dominio diferente. CORS consiste en agregar al servidor un conjunto específico de los encabezados que permiten a un navegador determinar si y cuándo se debe permitir solicitudes entre dominios.

Con los siguientes pasos, es muy sencillo habilitar esta opción, para poder permitir la conexión del API sin problemas de seguridad que imponen muchos navegadores Web, por seguridad, haciendo peticiones a dominios de terceros.

```shell
pip install django-cors-headers
```

```python
INSTALLED_APPS = (
    ...
    'corsheaders',
    ...
)
```

```python
MIDDLEWARE_CLASSES = (
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
```

### Probando el API RESTful

Ahora solo debemos ejecutar desde la línea de comandos, el runserver; lo que nos permitirá revisar adecuadamente los posibles errores de nuestro código y realizar las pruebas necesarias para asegurarnos de que funciona adecuadamente.

```shell
python3 manage.py runserver
```

Por último, desde el navegador ingresamos a la ruta indicada en el runserver, que comunmente es http://localhost:8000/ o hacer uso de clientes de solicitudes HTTP como Postman o similares, para realizar las solicitudes y pruebas correspondientes.

### Otras opciones y autenticación

El JSONParser no es la única opción de parseo que dispone la libreria de RESTFramework, también se puede usar: FormPaser, para las solicitudes que indican application/x-www-form-urlencoded cuando usamos un formulario tradicional; MultiPartParser, usado cuando enviamos archivos en las solicitudes al servidor; y se pueden hacer uso de varios otros e incluso personalizarlos.

Los métodos de autenticación son tan variados como los que existen a través de la red, de una forma sencilla podemos implementar el esquema de OAuth, OAuth2, JWT, Social OAuth además del Basic Authentication basico que es el utilizado en este ejemplo.

Además se pueden hacer uso de varias opciones más, cuando personalizamos nuestros servicios a través de sets de vistas que ya existan o que estemos realizando: renderer_classes, parser_classes, authentication_classes, throttle_classes, permission_classes, content_negotiation_class.

## Conclusiones

En proceso...
