FROM continuumio/miniconda3:4.7.12

# Création d'un utilisateur non Root
RUN adduser --disabled-password --gecos "Default user" --uid 1000 eggplant

# Partage des droits pour l'utilisation de conda
RUN mkdir /opt/conda/envs/eggplant /opt/conda/pkgs && \
    chgrp eggplant /opt/conda/pkgs && \
    chmod g+w /opt/conda/pkgs && \
    touch /opt/conda/pkgs/urls.txt && \
    chown eggplant /opt/conda/envs/eggplant /opt/conda/pkgs/urls.txt

USER 1000

# Création de l'env codna
ADD environment.yml /tmp/environment.yml

RUN conda env create -f /tmp/environment.yml

# Activation de l'env conda
SHELL ["conda", "run", "-n", "eggplant", "/bin/bash", "-c"]

# Déplacement des fichiers nécessaires pour le fonctionnement du conteneur
COPY . /app

WORKDIR /app

CMD python main.py
