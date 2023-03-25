FROM python:3.8.10

WORKDIR /usr/app/src

COPY src ./
COPY src/Pipfile Pipfile

USER root

RUN pip install pipenv
RUN pipenv install --deploy --system --skip-lock

EXPOSE 5000

CMD ["bash", "/app/startServer.sh"]