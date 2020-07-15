FROM continuumio/miniconda3:4.7.12

RUN adduser --disabled-password --gecos "Default user" --uid 1000 eggplant

RUN mkdir /opt/conda/envs/eggplant /opt/conda/pkgs && \
    chgrp eggplant /opt/conda/pkgs && \
    chmod g+w /opt/conda/pkgs && \
    touch /opt/conda/pkgs/urls.txt && \
    chown eggplant /opt/conda/envs/eggplant /opt/conda/pkgs/urls.txt

RUN mkdir -p /app

RUN chown -R eggplant:eggplant /app

RUN chmod 755 /app

USER 1000

ADD environment.yml /tmp/environment.yml

RUN conda env create -f /tmp/environment.yml

SHELL ["conda", "run", "-n", "eggplant", "/bin/bash", "-c"]

COPY . /app

WORKDIR /app

ARG APPLICATION_PROPERTIES

COPY ${APPLICATION_PROPERTIES} .env

RUN python trainModel.py

CMD python predictionLoop.py
