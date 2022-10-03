FROM debian:latest

ADD requirements.txt /tmp/requirements.txt
ADD /app/* /app/

RUN apt install -y python3 python3-pip
RUN pip3 install -r /tmp/requirements.txt

CMD [ "python3", "/app/main.py" ]
