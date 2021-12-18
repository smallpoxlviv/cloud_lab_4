FROM python:3.8

WORKDIR /sensors

RUN apt-get update -y 

RUN git clone https://github.com/smallpoxlviv/cloud_lab_4.git

WORKDIR /sensors/cloud_lab_4/containers_src/sensors
RUN pip3 install --upgrade pip -r requirements.txt

RUN chmod a+x run.sh

CMD ["./run.sh"]