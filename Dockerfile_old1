FROM alpine:3.14

# Install Nginx and remove default server definition
RUN apk add --no-cache nginx:1.19.0 \
    rm -rf /var/cache/apk/*

#COPY entrypoint.sh /root/entrypoint.sh

#RUN chmod 777 /root/entrypoint.sh

#ENTRYPOINT /root/entrypoint.sh

# Create necessary directories


# Copy custom configuration file (if needed)
# COPY nginx.conf /etc/nginx/nginx.conf
COPY ./index.html /usr/share/nginx/html
COPY ./nginx.conf /opt/homebrew/etc/nginx/nginx.conf

RUN mkdir -p /run/nginx

# Expose the default Nginx port
EXPOSE 3000

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]