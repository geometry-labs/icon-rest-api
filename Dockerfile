FROM python:3.8-slim as base

WORKDIR /app/

COPY ./requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/

FROM base as prod
CMD ["python3", "./main.py"]

FROM base as test
RUN pip install -r /requirements_dev.txt
RUN python -m pytest
