FROM python:3.12-slim-bookworm AS base
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends curl git build-essential \
    && apt-get autoremove -y

FROM base AS install
WORKDIR /home/code


FROM install as app-image

ENV PYTHONPATH=/home/code/ PYTHONHASHSEED=0

#COPY tests/ tests/
COPY app/ app/
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN pwd
# create a non-root user and switch to it, for security.
#RUN addgroup --system --gid 999 "docker"
#RUN adduser --system --uid 999 "app-user"
RUN mkdir /home/code/output 
#&& chown -R app-user:docker /home/code/output

#USER "app-user"
