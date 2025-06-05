# FROM python:3.10.8-alpine
# RUN apk add python3-dev build-base linux-headers pcre-dev mariadb-connector-c-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
# RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl libmemcached-dev
# RUN pip install uwsgi

FROM python:3.11
ARG DEBIAN_FRONTEND=noninteractive
# RUN apk add python3-dev gpgme-dev libc-dev build-base linux-headers pcre-dev mariadb-connector-c-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev pkgconfig
# RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl firefox

RUN apt-get update

RUN pip install uwsgi


# Install selenium
RUN pip install --upgrade pip \
 && pip install selenium

# set display port to avoid crash
ENV DISPLAY=:99

# create the app user
#RUN addgroup -S app && adduser -S app -G app

ENV WORK=/etc/app
ENV WORK_HOME=/etc/app
RUN mkdir $WORK_HOME
WORKDIR $WORK_HOME

COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ ./

RUN chown -R nobody:nogroup $WORK_HOME/db.sqlite3

RUN chown -R nobody:nogroup $WORK_HOME

RUN chmod a+rw db.sqlite3 $WORK_HOME/db.sqlite3

CMD python manage.py migrate

CMD ["uwsgi", "--chdir=/etc/app", "--module=charity.wsgi:application", "--enable-threads" , "--master", "--pidfile=/tmp/project-master.pid", "--http=0.0.0.0:8000", "--processes=5", "--uid=1000", "--gid=2000", "--harakiri=20", "--max-requests=5000", "--vacuum"]

VOLUME /public
VOLUME /uploads
VOLUME /db
