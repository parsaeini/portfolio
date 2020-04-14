FROM python:3.8

RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install gunicorn
ADD . /code/

CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8000 portfolio.wsgi:application
