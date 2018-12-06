FROM python:3.7-alpine
COPY ./app /app
WORKDIR /app
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers
RUN pip install -r requirements.txt
RUN apk del .build-deps
CMD ["uwsgi", "--ini", "app.ini"]