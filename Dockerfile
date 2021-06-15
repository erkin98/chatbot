# syntax=docker/dockerfile:1

FROM python:3.9.5-alpine
WORKDIR /code
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]