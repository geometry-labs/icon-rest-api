FROM python:3.8-slim as base

WORKDIR /src/

COPY ./requirements.txt /requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

FROM base as prod
CMD ["python3", "./main.py"]

FROM base as test
COPY ./requirements_dev.txt /requirements_dev.txt
RUN pip install -r /requirements_dev.txt

# Run tests manually by execing into container in CI
#RUN python -m pytest
