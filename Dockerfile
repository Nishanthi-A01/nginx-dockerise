FROM nginx:1.19-alpine

#COPY entrypoint.sh /root/entrypoint.sh

#RUN chmod 777 /root/entrypoint.sh

#ENTRYPOINT /root/entrypoint.sh

ENV NGINX_VERSION=1.19.10 \
    PKG_RELEASE=1 \
    APP_HOME=/usr/local/share/nginx/html

COPY ./index.html $APP_HOME

COPY ./nginx.conf /etc/nginx/nginx.conf


EXPOSE 3000

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]





