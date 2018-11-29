FROM python:3.6.4-alpine3.7

RUN apk update && apk add \
        postgresql-dev \
        python3-dev \
        gcc \
        nano \
        gfortran \
        py-pip \
        build-base \
        wget \
        freetype-dev \
        libpng-dev \
        openblas-dev \
        jpeg-dev \
        zlib-dev \
        musl-dev \
        linux-headers && \
        mkdir app


WORKDIR /app/

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

ADD . /app/

RUN if [ -s requirements.txt ]; then pip install --upgrade pip; fi
RUN if [ -s requirements.txt ]; then pip install -r requirements.txt; fi
EXPOSE 8092
VOLUME /app/pubcloud/assets
ENTRYPOINT ["/usr/local/bin/uwsgi", "--ini", "/app/uwsgi.ini"]
