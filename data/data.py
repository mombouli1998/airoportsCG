import pandas as pd

# Lecture du fichier CSV contenant les données des aéroports
ts = pd.read_csv('cg-airoports.csv')
ts = ts.drop(index=0)  # Supprime la première ligne du DataFrame (souvent une ligne d'entête redondante)

# Nettoyage des données
colonnes_a_supprimer = [
    'continent', 'country_name', 'iso_country', 'gps_code', 'icao_code',
    'keywords', 'ident', 'iata_code', 'local_code', 'home_link', 'wikipedia_link'
]  # Liste des colonnes à supprimer car jugées inutiles
ts.drop(columns=colonnes_a_supprimer, inplace=True)  # Suppression des colonnes non pertinentes

ts["region_name"] = ts["region_name"].str.replace("Department", "", regex=False)  # Supprime le mot "Department" dans la colonne 'region_name'
ts["region_name"] = ts["region_name"].str.strip()  # Supprime les espaces au début et à la fin des chaînes dans la colonne 'region_name'
ts["last_updated"] = pd.to_datetime(ts["last_updated"], errors='coerce').dt.year  # Convertit la colonne 'last_updated' en datetime et extrait uniquement l'année

# Création des DataFrames airoports et regions à partir des colonnes pertinentes
airports = ts[['id', 'type', 'name', 'municipality', 'score', 'last_updated']]
municipalities = ts[['municipality', 'region_name', 'latitude_deg', 'longitude_deg', 'elevation_ft']]

# Affichage des 5 premières lignes des DataFrames
print(airports.head())  # Affiche les 5 premières lignes du DataFrame 'airoports'
print(municipalities.head())  # Affiche les 5 premières lignes du DataFrame 'regions'

# Enregistrement des DataFrames dans des fichiers CSV
airports.to_csv('airports.csv', index=False)  # Enregistre le DataFrame 'airoports' dans un fichier CSV
municipalities.to_csv('municipalities.csv', index=False)  # Enregistre le DataFrame 'regions' dans un fichier CSV
