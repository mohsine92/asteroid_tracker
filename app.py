import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

# ------------------------------
# 🚀 1. Titre et description
# ------------------------------
st.set_page_config(page_title="NASA Asteroid Tracker", layout="centered")
st.title("NASA Asteroid Tracker")
st.write("Visualisation des astéroïdes proches de la Terre à partir des données publiques de la NASA.")

# ------------------------------
# 🌍 2. Paramètres utilisateur
# ------------------------------
# Clé API depuis variable d'environnement, fallback sur DEMO_KEY
API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

st.info("""
ℹ️ Pour des volumes de données plus importants, utilisez votre clé NASA personnelle.
DEMO_KEY : limité à 30 requêtes/h et 1000/jour.
Créez votre clé sur [NASA API](https://api.nasa.gov)
""")

start_date = st.date_input("Date de début", pd.to_datetime("2025-08-20"))
end_date = st.date_input("Date de fin", pd.to_datetime("2025-08-25"))

# ------------------------------
# 📡 3. Récupération des données NASA
# ------------------------------
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()  # déclenche une exception si code != 200
    data = response.json()
    
    asteroid_list = []
    for date, asteroids in data["near_earth_objects"].items():
        for asteroid in asteroids:
            asteroid_list.append({
                "date": date,
                "name": asteroid['name'],
                "diameter_m": asteroid['estimated_diameter']['meters']['estimated_diameter_max'],
                "hazardous": asteroid['is_potentially_hazardous_asteroid']
            })

    df = pd.DataFrame(asteroid_list)

    # ------------------------------
    # 📊 4. Tableau interactif
    # ------------------------------
    st.subheader("📋 Données brutes")
    st.dataframe(df)

    # ------------------------------
    # 📈 5. Visualisation
    # ------------------------------
    st.subheader("📈 Taille des astéroïdes par date")
    fig, ax = plt.subplots()
    colors = df["hazardous"].map({True: "red", False: "green"})
    ax.scatter(df["date"], df["diameter_m"], c=colors, s=100, alpha=0.7)
    ax.set_title("Astéroïdes proches de la Terre")
    ax.set_xlabel("Date de passage")
    ax.set_ylabel("Diamètre (m)")
    plt.xticks(rotation=45)
    st.pyplot(fig)


    # Alertes
    st.subheader("🚨 Astéroïdes dangereux détectés")
    dangerous = df[df["hazardous"] == True]
    if not dangerous.empty:
        st.error(f"{len(dangerous)} astéroïdes dangereux détectés ⚠️")
        st.table(dangerous[["date", "name", "diameter_m"]])
    else:
        st.success("Aucun astéroïde dangereux sur cette période ✅")

except requests.exceptions.HTTPError:
    if response.status_code == 403:
        st.error("🚨 Quota API atteint. Merci de créer votre propre clé NASA pour continuer.")
    else:
        st.error(f"Erreur {response.status_code} lors de la récupération des données NASA.")
except requests.exceptions.RequestException as e:
    st.error(f"Erreur réseau : {e}")
except KeyError:
    st.error("Erreur inattendue : format des données NASA inconnu.")