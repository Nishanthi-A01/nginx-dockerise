FROM nginx:1.19-alpine

RUN addgroup -S nisha && adduser -S nisha -G nginx


USER nisha

ENV NGINX_VERSION=1.19.10 \
    PKG_RELEASE=1 \
    APP_HOME=/usr/share/nginx/html



COPY index.html $APP_HOME/

COPY ./nginx.conf /opt/homebrew/etc/nginx/nginx.conf

RUN chown -R nisha:nginx $APP_HOME



EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]




