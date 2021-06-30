FROM python:3.7-alpine
LABEL Daniel Eduardo Canon

ENV PYTHONUNBUFFERED 1

COPY ./base/requirements /requirements
# psycopg2 and pillow dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev \
        python3-dev 
RUN apk add jpeg-dev zlib-dev
# telnet
RUN apk add busybox-extras
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements/dev.txt

# new entrypoint
COPY ./base/compose/dev/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

RUN apk del .tmp-build-deps

RUN mkdir /app
COPY ./base/app /app
WORKDIR /app
ENTRYPOINT ["/entrypoint"]

