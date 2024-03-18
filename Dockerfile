# Use an official Python runtime as a parent image
FROM python:3.7
LABEL maintainer="hello@wagtail.io"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
# apt-get install apache2-dev
# Install any needed packages specified in requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

CMD apt-get install redis-server
CMD service redis-server start
RUN python manage.py migrate
RUN python manage.py crontab add

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
CMD exec gunicorn iitg_mechanical_website.wsgi:application --bind 0.0.0.0:8000 --workers 3
# RUN python manage.py crontab add
# RUN celery -A iitg_mechanical_website worker -l info