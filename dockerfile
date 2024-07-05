FROM python:3.12.3-alpine3.20

WORKDIR /code

RUN apk update && apk upgrade
COPY requirements.txt /code/requirements.txt

RUN pip3 install -r /code/requirements.txt --no-cache-dir --no-warn-script-location
COPY ./source /code/source

CMD ["fastapi", "run", "source/api.py", "--port", "80", "--proxy-headers"]
