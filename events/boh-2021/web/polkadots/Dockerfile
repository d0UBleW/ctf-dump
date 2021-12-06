FROM php:7.2-fpm-alpine

LABEL Author="redblaze"

COPY files /tmp/

RUN apk add --update --no-cache nginx \
    && mkdir /run/nginx \
    && mv /tmp/docker-entrypoint /usr/local/bin/docker-entrypoint \
    && mv /tmp/nginx.conf /etc/nginx/nginx.conf \
    && mv /tmp/vhost.nginx.conf /etc/nginx/conf.d/default.conf \
    && mv /tmp/src/* /var/www/html \
    && chmod -R 755 /var/www/html \
    && chown -R www-data:www-data /var/www/html \
    && rm -rf /tmp/* \
    && rm -rf /etc/apk

EXPOSE 80

VOLUME ["/var/log/nginx"]

CMD ["/bin/sh", "-c", "docker-entrypoint"]