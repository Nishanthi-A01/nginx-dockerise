FROM nginx:1.19.0

WORKDIR /app

COPY index.html .
COPY images ./images
COPY ./nginx.conf /opt/homebrew/etc/nginx/nginx.conf



EXPOSE 3000




