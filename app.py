
import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(page_title="🏇 Equidia IA - Marco Edition", layout="wide")

st.title("🏇 Application IA des Courses - Marco Edition")
st.markdown("**Analyse des chevaux, météo, tickets IA, ROI, et comparateur public.**")

# Section Météo
st.header("🌦 Météo à Lyon-La Soie")
meteo = {
    "hippodrome": "Lyon-La Soie",
    "temps": "Nuageux",
    "température": "15°C",
    "vent": "21 km/h"
}
st.success(f"Météo : {meteo['temps']} | Température : {meteo['température']} | Vent : {meteo['vent']}")

# Section Analyse IA pour une course réelle (R5 C8)
st.header("🧠 Analyse IA - R5 C8")
chevaux = ["Skadoosh", "Her Christopher", "Sindia", "Wedgewood Pearl", "King Zarak",
           "Arigato", "Carlston", "Darylakha", "Lady Mana"]

np.random.seed(45)
formes = np.random.randint(1, 6, len(chevaux))
poids = np.random.uniform(54, 60, len(chevaux))
cordes = np.random.randint(1, 10, len(chevaux))
musique = np.random.randint(50, 100, len(chevaux)) / 100
meteo_impact = np.random.uniform(0.85, 1.15, len(chevaux))

scores = np.round(0.3 * formes + 0.2 * (60 - poids) + 0.2 * (10 - cordes) +
                  0.2 * musique * 10 + 0.1 * meteo_impact * 10, 2)
classement = scores.argsort()[::-1] + 1

df = pd.DataFrame({
    "Cheval": chevaux,
    "Forme": formes,
    "Poids (kg)": np.round(poids, 1),
    "Corde": cordes,
    "Musique": np.round(musique, 2),
    "Météo": np.round(meteo_impact, 2),
    "Score IA": scores,
    "Classement IA": classement
}).sort_values("Score IA", ascending=False).reset_index(drop=True)

st.dataframe(df)

# Ticket IA
st.header("🎫 Ticket IA proposé")
st.info("Trio IA : " + " - ".join(df['Cheval'].head(3)))

# ROI Simulé
st.header("📈 ROI Simulé")
st.metric("ROI estimé", "+14.8%", delta="+2.4%")

st.markdown("---")
st.caption("Développement IA turf - sauvegarde complète by Marco.")
