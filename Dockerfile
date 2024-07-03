# https://fastapi.tiangolo.com/deployment/docker/

FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./.env.local /code/.env.local
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./App /code/App

#CMD ["fastapi", "run", "App/main.py", "--port", "8000"]
CMD ["uvicorn", "main:app", "--port=80", "--host=0.0.0.0", "--root-path=/api"]