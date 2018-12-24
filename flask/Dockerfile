FROM python:3.7-alpine
COPY ./app /app
WORKDIR /app
RUN apk add uwsgi-python3 
RUN pip install -r requirements.txt
ENV PYTHONPATH /usr/local/lib/python3.7/site-packages:/usr/lib/python3.6/site-packages
CMD ["uwsgi", "--ini", "app.ini"]