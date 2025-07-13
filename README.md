# ✈️ Aéroport API – Données des aéroports du Congo

Bienvenue dans **Aéroport API**, une API RESTful développée avec **FastAPI** permettant d’explorer, filtrer et analyser les aéroports et municipalités du **Congo** à partir de données géographiques nettoyées.

---

## 🧰 Fonctionnalités principales

- 📋 Liste complète des aéroports et municipalités
- 🔍 Filtres sur les aéroports : type, municipalité, score, année de mise à jour
- 🗺️ Recherche géographique (latitude, longitude, élévation)
- 📊 Statistiques globales (comptes par région/type, top 5 élévation)
- 📍 Regroupement des municipalités par région
- 📌 Analyse globale : nombre total d’aéroports, municipalités, régions

---

## ⚙️ Prérequis

- Python ≥ 3.10
- SQLite3
- Client HTTP comme `httpx`, `requests`, ou Postman

### Installation rapide de `httpx` :

```bash
pip install httpx
````
### 🚀 Démarrage de l’API :
```
python3 -m uvicorn main:app --reload
````
## Accès à l’API :
- API Root : http://localhost:8000
- Swagger UI : http://localhost:8000/docs

### 📦 Endpoints disponibles

## 📦 Endpoints disponibles

| Méthode | URL | Description |
|--------|-----|-------------|
| GET | `/` | Test de fonctionnement de l’API |
| GET | `/airoports` | Liste de tous les aéroports |
| GET | `/airoports/filter` | Recherche d’aéroports par filtres (type, municipalité, score, année) |
| GET | `/airoports/type/{type}` | Recherche d’aéroports par type |
| GET | `/airoports/updated/{year}` | Aéroports mis à jour après une année donnée |
| GET | `/airoports/top5_elevation` | Top 5 des aéroports les plus élevés |
| GET | `/airoports/count_by_region` | Nombre d’aéroports par région |
| GET | `/airoports/count_by_type` | Nombre d’aéroports par type |
| GET | `/airoports/types_by_region` | Répartition des types d’aéroports par région |
| GET | `/municipalities` | Liste des municipalités |
| GET | `/municipalities/by_region` | Municipalités regroupées par région |
| GET | `/municipalities/lat_long_score` | Coordonnées et scores des municipalités |
| GET | `/regions` | Liste des régions |
| GET | `/analysis/result` | Analyse globale : nombre d’aéroports, municipalités, régions |

## 📂 Structure des données

Les données sont extraites d’un fichier CSV `cg-airoports.csv`, nettoyées avec **Pandas**, puis injectées dans une base de données **SQLite** nommée `airportsCongo.db`.

### 🗄️ Tables de la base de données

#### ✈️ Table `airports`
Contient les informations principales sur les aéroports.

| Champ | Type | Description |
|-------|------|-------------|
| `id` | INTEGER (Primary Key) | Identifiant unique de l’aéroport |
| `type` | TEXT | Type d’aéroport (ex: small_airport, medium_airport) |
| `name` | TEXT | Nom de l’aéroport |
| `municipality` | TEXT | Ville ou municipalité de l’aéroport |
| `score` | INTEGER | Score ou note de l’aéroport |
| `last_updated` | INTEGER (Année) | Année de la dernière mise à jour |

#### 🏙️ Table `municipalities`
Contient des données géographiques et administratives sur les municipalités.

| Champ | Type | Description |
|-------|------|-------------|
| `municipality` | TEXT (Primary Key) | Nom de la municipalité |
| `region_name` | TEXT | Région administrative à laquelle appartient la municipalité |
| `latitude_deg` | REAL | Latitude en degrés |
| `longitude_deg` | REAL | Longitude en degrés |
| `elevation_ft` | INTEGER | Altitude en pieds |

### 🧪 Exemples d’utilisation avec httpx
import httpx

# Obtenir les aéroports filtrés
params = {"type": "small_airport", "score": 5}
response = httpx.get("http://localhost:8000/airoports/filter", params=params)
print(response.json())

# Obtenir les 5 aéroports les plus élevés
response = httpx.get("http://localhost:8000/airoports/top5_elevation")
print(response.json())

## 📚 Ressources utiles

- 🔍 **Interface Swagger** (documentation interactive de l'API) :  
  [http://localhost:8000/docs](http://localhost:8000/docs)

- 📊 **Données brutes utilisées** (aéroports) :  
  [https://ourairports.com/data](https://data.humdata.org/dataset/ourairports-cog)

## 👨‍💻 Auteur

Développé par **MOMBOULI Trinité**  
📧 [trinitemombouli@gmail.com](mailto:trinitemombouli@gmail.com)



 
