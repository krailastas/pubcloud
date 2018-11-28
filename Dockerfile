FROM python:3.6.4-alpine3.7

RUN apk update && apk add --no-cache --virtual .build-deps \
        gcc \
        make \
        nano \
        python3-dev \
        linux-headers \
        musl-dev \
        postgresql-dev \
        && pip install --no-cache-dir psycopg2 \
        && apk del --no-cache .build-deps

WORKDIR /app/

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

ADD . /app/

RUN if [ -s requirements.txt ]; then pip install -r requirements.txt; fi
EXPOSE 8092
VOLUME /app/pubcloud/assets
ENTRYPOINT ["/usr/local/bin/uwsgi", "--ini", "/app/uwsgi.ini"]
