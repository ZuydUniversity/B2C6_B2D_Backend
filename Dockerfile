# https://fastapi.tiangolo.com/deployment/docker/

FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./App /code/App

CMD ["fastapi", "run", "App/main.py", "--port", "80"]