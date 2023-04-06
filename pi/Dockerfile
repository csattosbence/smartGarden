FROM python:3.8.10

WORKDIR /usr/app/src

COPY src ./
COPY src/Pipfile Pipfile

USER root

RUN pip install pipenv
RUN pip install numpy
RUN pip install flask-swagger
RUN pip install flask-swagger-ui
RUN pip install Flask-SocketIO==5.2.0
RUN pip install simple-websocket
RUN pipenv install --deploy --system --skip-lock

EXPOSE 5000

CMD ["bash", "/app/startServer.sh"]