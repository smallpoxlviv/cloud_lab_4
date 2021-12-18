FROM python:3.8

WORKDIR /backend

RUN apt-get update -y 

RUN git clone https://github.com/smallpoxlviv/cloud_lab_4.git

WORKDIR /backend/cloud_lab_4/containers_src/backend
RUN pip3 install --upgrade pip -r requirements.txt
RUN pip3 --no-cache-dir install --upgrade awscli
RUN pip3 install gunicorn

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "index:app"]