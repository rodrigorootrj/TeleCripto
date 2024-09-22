FROM python:3.10
RUN mkdir /app/ /assets/
COPY doc/asset/requirements.txt /assets/
WORKDIR /app/
RUN pip install -r /assets/requirements.txt