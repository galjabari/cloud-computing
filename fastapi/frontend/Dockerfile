# Use a lightweight web server as the base image
FROM nginx:alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY src/ /usr/share/nginx/html
EXPOSE 80