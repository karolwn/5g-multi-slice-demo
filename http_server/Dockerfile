# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080 
RUN apt-get update
RUN apt-get install -y gcc musl-dev linux-headers-amd64 iperf3 hping3 bwm-ng net-tools iputils-ping iperf
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["flask", "run"]
