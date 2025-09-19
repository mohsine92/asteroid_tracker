# ---------------------------------------------------------------
# Asteroid Tracker
# ---------------------------------------------------------------
# Features:
# - Choose a specific date to visualize detected asteroids.
# - Displays key information: name, size, velocity, and distance from Earth.
# - Graphical insights to better understand asteroid trajectories.
#
# Note:
# - NASA API only allows querying a limited date range (usually up to 7 days).
# - Data availability may vary depending on NASA’s latest updates.
#
# Author   : Mohsine Essat
# Date     : August 2025
# Tech     : Python, Streamlit, Pandas, Matplotlib, NASA NeoWS API
# ---------------------------------------------------------------

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np



# API key from environment variable
API_KEY = st.secrets["NASA_API_KEY"]



# Title and description
st.set_page_config(page_title="NEO Watch - Asteroid Tracker Dashboard", layout="centered")
st.title("NEO Watch - Asteroid Tracker Dashboard")
st.write("Visualization of near-Earth asteroids based on public data from NASA.")
st.write("This project was born out of my passion for the engineering behind space observation tools. It stems from a desire to understand, model, represent, and make accessible real astronomical phenomena, particularly near-Earth objects (NEOs).")
st.write("This project is a scaled-down version of the NEO Surveyor mission. NEO Surveyor is the first space telescope designed specifically to detect potentially hazardous asteroids and comets.")
st.markdown('<a href="mailto:mohsine.essat@gmail.com">Contact me !</a>', unsafe_allow_html=True)
st.link_button("Linkedin", "https://www.linkedin.com/in/mohsine-essat/")
st.link_button("GitHub", "https://github.com/mohsine92/asteroid_tracker")


# Information

st.info("""
Note :  For larger data volumes, use your personal NASA key. Create your key on (https://api.nasa.gov)
- NASA API only allows querying a limited date range (usually up to 7 days).
""")


start_date = st.date_input("From", pd.to_datetime("2025-08-20"))
end_date = st.date_input("To", pd.to_datetime("2025-08-22"))



# Récupération des données NASA
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"

try:
    response = requests.get(url)
    response.raise_for_status()  # throws an exception if code != 200
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

    # Interactive whiteboard
    st.subheader("Raw data")
    st.dataframe(df)

    # Visualization

## futur polar plot ###

    # Date of visit - Diameter/Metre
    st.subheader("Asteroid size by date")
    fig, ax = plt.subplots()
    colors = df["hazardous"].map({True: "red", False: "green"})
    ax.scatter(df["date"], df["diameter_m"], c=colors, s=100, alpha=0.7)
    ax.set_title("Near-Earth asteroids")
    ax.set_xlabel("Date of visit")
    ax.set_ylabel("Diameter (m)")
    plt.xticks(rotation=45)
    st.pyplot(fig)


    # Alerts
    st.subheader("Close approach of asteroids detected")
    dangerous = df[df["hazardous"] == True]
    if not dangerous.empty:
        st.markdown(f"{len(dangerous)} asteroids passing safely close to Earth have been detected.")
        st.table(dangerous[["date", "name", "diameter_m"]])
    else:
        st.success("No asteroids near Earth during this period.")

except requests.exceptions.HTTPError:
    if response.status_code == 403:
        st.error("🚨 API quota reached. Please create your own NASA key to continue.")
    else:
        st.error(f"Error {response.status_code} while retrieving NASA data.")
except requests.exceptions.RequestException as e:
    st.error(f"Network error : {e}")
except KeyError:
    st.error("Unexpected error: unknown NASA data format.")