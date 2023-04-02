FROM python:3.10-alpine

LABEL maintainer="rami2sfari@gmail.com"

COPY ./requirement.txt /requirement.txt
RUN pip install -r /requirement.txt

COPY ./src /src

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
