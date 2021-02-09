FROM python:3.8-slim

WORKDIR /app/

COPY ./requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

CMD ["python3", "./main.py"]
