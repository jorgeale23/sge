FROM python:3.8-slim
WORKDIR /sge
COPY sge/ . 
# You will need this if you need PostgreSQL, otherwise just skip this
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN apt-get update -y
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y gcc
RUN pip install -r requirements.txt
# Installing uwsgi server
RUN pip install uwsgi
EXPOSE 8000
# This is not the best way to DO, SEE BELOW!!
#CMD uwsgi --http "0.0.0.0:8000" --master --enable-threads --module sge.wsgi
CMD python3 manage.py runserver
