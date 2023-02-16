FROM python:3

WORKDIR /code

COPY requeriments.txt /code/

RUN pip install -r requeriments.txt

COPY . /code/

# port where the Django app runs  
EXPOSE 8000  
# start server  
CMD python manage.py runserver
