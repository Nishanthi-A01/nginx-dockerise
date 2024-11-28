FROM nginx:1.19-alpine

RUN addgroup -S nisha && adduser -S nisha -G nginx


USER nisha

ENV NGINX_VERSION=1.19.10 \
    PKG_RELEASE=1 \
    APP_HOME=/usr/share/nginx/html

RUN chown -R nisha:nginx $APP_HOME

COPY index.html $APP_HOME/
COPY images ./images
COPY ./nginx.conf /opt/homebrew/etc/nginx/nginx.conf



EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]




