FROM python:3.8.10
WORKDIR /code

COPY /app /code/app
COPY ./requirements.txt /code/requirements.txt
COPY ./run.py /code/run.py
COPY ./.env /code/.env

ARG harded_apikey
ARG app_title
ARG app_description
ARG app_version

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8081/tcp

CMD ["python", "run.py"]
