# syntax=docker/dockerfile:1

FROM python:3.9.5-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk update \
apk add --virtual build-deps gcc g++ python3-dev musl-dev \
apk add postgresql-dev \
apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
apk add libffi-dev py-cffi \
RUN apk add --no-cache linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]