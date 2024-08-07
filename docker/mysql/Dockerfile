FROM mysql:latest

ENV MYSQL_DATABASE=${DB_NAME}
ENV MYSQL_ROOT_PASSWORD=${DB_PASSWORD}

COPY ./init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
