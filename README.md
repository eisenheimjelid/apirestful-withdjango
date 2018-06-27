# Sample project for a RESTFul API with REST Framework and Django

![Django Logo](django-logo.png)

![Django 2.0](https://img.shields.io/badge/django-2.0-green.svg) | [![Follow on Twitter](twitter-logo.png)](https://twitter.com/jelidleon) [@jelidleon](https://twitter.com/jelidleon)

Example project, tutorial type about **how to use django-restframework**, using the serialization classes of models and customized views to perform any type of operation (GET, POST, OPTIONS, etc.), and using Docker.

Read this content in other languages: [English](README.md), [Español](README.es-MX.md)

## Content

Next, the process is described, in order to get a code similar to the one shared in the example in this repository.

### Doing magic (Docker + pip)

**PIP** is a tool that will allow us to have all the necessary packages and dependencies, in this case we will use the ones that are in the list of `requirements.pip`.

**Docker** is a tool that will allow us to have all the necessary software to have our full development environment.

```shell
$ sudo docker-compose build
```

### Configuring Django

Now we must make the necessary configuration of the settings, in order to properly use the restframework package.

With the `settings.py` file

```python
INSTALLED_APPS = [
    'jet',
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
        'NAME': os.path.join (BASE_DIR, 'db.sqlite3'),
    }
}

.
.
.

STATIC_ROOT = 'html /'
STATIC_URL = '/ static /'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

```

**_ more changes, soon ... _**

### Creating models, functions and some classes

Then we proceed to create some models, to properly complete the example, as well as some functions and other classes, for a personalized service and also to use the serializers with the basic models of django Auth.

In the `models.py` file we define the own models, define the necessary ones in other 'webapps'

```python
CONTACT_TYPES = (
    ('Issuer', 'Issuer'),
    ('Receiver', 'Receiver'),
)


class Service (models.Model):
    name = models.CharField (max_length = 1024, null = True, blank = True)
    description = models.TextField (null = True, blank = True)
    .
    .
    .
```

With the file `serializers.py` we define the classes that will be used to serialize the models that were defined in the previous file.

```python
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Goal:
        model = User
        fields = ('url', 'username', 'email', 'groups')
    .
    .
    .
```

With the file `urls.py` we register each set of serialized views, in the corresponding router with the names that we define according to the use of each one.

```python
.
.
.
class UserViewSet (viewsets.ModelViewSet):
    """
    API service to view or edit system users
    """
    queryset = User.objects.all (). order_by ('- date_joined')
    serializer_class = UserSerializer
    .
    .
    .
```

### CSRF ?? CORS ??

The protection *Cross Site Request Forgery* is a protection mechanism against a particular type of attack, which can occur when a user has not closed a website session, and still has a valid session. In this circumstance a malicious site may be able to perform actions against the destination site, in the context of the session initiated session.

A clear example of the above is when we disable the control in our example (line 35 urls.py) or try to send a request to a POST / PUT service without the corresponding token.

The *Cross-Origin Resource Sharing* mechanism is a mechanism to allow clients to interact with APIs that are hosted in a different domain. CORS consists of adding to the server a specific set of headers that allow a browser to determine if and when requests should be allowed between domains.

With the following steps, it is very easy to enable this option, in order to allow the API connection without security problems imposed by many Web browsers, for security, making requests to third-party domains.

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

### Testing the RESTful API

Now we just have to run from the command line, the runserver; which will allow us to adequately review the possible errors of our code and perform the necessary tests

```shell
python3 manage.py runserver
```

Finally, from the browser we enter the route indicated in the runserver, which is commonly http: // localhost: 8000 / or make use of HTTP request clients such as Postman or similar, to make the corresponding requests and tests.

### Other options and authentication

The JSONParser is not the only parsing option available in the RESTFramework library, you can also use: FormPaser, for requests that indicate application / x-www-form-urlencoded when using a traditional form; MultiPartParser, used when we send files in requests to the server; and you can make use of several others and even customize them.

The authentication methods are as varied as those that exist through the network, in a simple way we can implement the OAuth, OAuth2, JWT, Social OAuth scheme in addition to the Basic Basic Authentication that is used in this example.

In addition you can make use of several other options, when we customize our services through sets of views that already exist or that we are doing: renderer_classes, parser_classes, authentication_classes, throttle_classes, permission_classes, content_negotiation_class.

## Conclusions

**_ still in process _**
