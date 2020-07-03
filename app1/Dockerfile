FROM python:3.8
RUN apt-get update && apt-get install -y python3-pip
COPY . .
RUN pip3 install flask
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]
