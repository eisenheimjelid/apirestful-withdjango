FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir -p /var/www/manager/static
RUN mkdir -p /var/www/manager/upload
WORKDIR /code
ADD config/requirements.pip /code/
RUN pip install -r requirements.pip
ADD ./manager /code/
ADD ./manager/static /var/www/manager/static
ADD ./manager/upload /var/www/manager/upload
ADD ./manager/templates /var/www/manager/templates
