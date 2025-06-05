FROM python:3.11-slim
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get update && apt-get install -y \
  default-libmysqlclient-dev wget libxml2 libxslt1-dev\
  pkg-config \
  gcc \
  pkg-config \
  && rm -rf /var/lib/apt/lists/*
  
RUN pip install -U pip uwsgi

ENV WORK=/etc/app
ENV WORK_HOME=/etc/app
RUN mkdir $WORK_HOME
WORKDIR $WORK_HOME

COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ ./

RUN chmod 777 /root

RUN python manage.py migrate

CMD ["uwsgi", "--chdir=/etc/app", "--module=charity.wsgi:application", "--enable-threads" , "--master", "--pidfile=/tmp/project-master.pid", "--http=0.0.0.0:8000", "--processes=5", "--uid=1000", "--gid=2000", "--harakiri=20", "--max-requests=5000", "--vacuum"]

EXPOSE 6379
EXPOSE 11211

VOLUME /public
VOLUME /uploads

