import streamlit as st
import pandas as pd


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url, delimiter=';')
    # Convert the 'Date/Time' column to datetime format
    df = df.dropna(subset=['consommation_brute_gaz_grtgaz'])
    df['date'] = pd.to_datetime(df['date'])
    df['date_heure'] = pd.to_datetime(df['date_heure'])
    df['heure'] = pd.to_datetime(df['heure'], format='%H:%M', errors='coerce').dt.time
    return df


df = load_data(
    "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/consommation-quotidienne-brute/exports/csv")
st.dataframe(df.head())


st.button("Rerun")
