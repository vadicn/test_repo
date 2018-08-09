FROM python:3.4.2-slim
RUN mkdir -p /var/app
WORKDIR /var/app
ADD requirements.txt /var/app
RUN pip install -r requirements.txt
COPY . /var/app
CMD python manage.py runserver 0.0.0.0:8080