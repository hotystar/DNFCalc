# Builds a Docker image, extending from the official nginx image, that contains
# custom configuration.
#
FROM ubuntu:latest
MAINTAINER ity <bju11@naver.com>

RUN apt-get update
RUN apt-get install -y python python-pip nginx

RUN pip install uwsgi

RUN ln -s /usr/local/bin/uwsgi /usr/bin/uwsgi

ADD ubuntu/uwsgi.ini /uwsgi.ini

RUN rm /etc/nginx/sites-available/default
COPY ubuntu/default /etc/nginx/sites-available/default

COPY ubuntu/1_dnfdg.xyz_bundle.crt /etc/nginx/ssl/1_dnfdg.xyz_bundle.crt

RUN pip2 install --upgrade pip

COPY ubuntu/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

VOLUME ["/home/ubuntu/dfcalc"]

EXPOSE 80
EXPOSE 443

ADD ubuntu/start.sh /start.sh
CMD ["/start.sh"]