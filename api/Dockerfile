# Utilise une image légère de python 3.13.5 comme base

FROM python:3.13.5-slim

## Définit le repertoire de travail dans le conteneur
WORKDIR /app

## Copie le fichier des dépendances dans le conteneur

COPY requirements.txt .

## Installe les dépendances sans mise en cache

RUN pip install  --no-cache-dir --upgrade -r requirements.txt

## COPY tous les fichiers .py et le fichier .db dans le conteneur

COPY . .

## Lance le serveur uvicorn pur executer l'api  fast api

CMD ["python3","-m","uvicorn","main:app","--host","0.0.0.0","--port","80"]