FROM nvidia/cuda:11.8.0-runtime-ubuntu22.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y iproute2 procps

COPY monitor.sh .
RUN chmod +x monitor.sh

CMD ["./monitor.sh"]