FROM ubuntu
WORKDIR /usr/src/ubook

RUN apt update
RUN apt upgrade -y
RUN apt install -y software-properties-common curl
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.10 python3-pip python3.10-distutils

COPY . .

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]