FROM nginx:1.19.0

WORKDIR /app

COPY server.js .
COPY index.html .
COPY images ./images
COPY package.json .
COPY ./nginx.conf /opt/homebrew/etc/nginx/nginx.conf

RUN npm install



EXPOSE 3000




