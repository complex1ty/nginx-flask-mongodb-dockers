FROM python:3.7-alpine
ADD ./app /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]