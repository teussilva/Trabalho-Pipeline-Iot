
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

DB_USER = 'postgres'
DB_PASSWORD = '12345'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iot_db'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

st.set_page_config(page_title="Dashboard IoT", layout="wide")
st.title("Dashboard de Temperatura IoT")

#@st.cache_data
def load_data():
    query = "SELECT * FROM temperature_readings;"
    df = pd.read_sql(query, engine)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

st.subheader("Visualização de dados")
st.dataframe(df.head(10))

# ---------- Filtros ----------
st.sidebar.header("Filtros")
devices = st.sidebar.multiselect(
    "Selecione dispositivos",
    options=df['device_name'].unique(),
    default=df['device_name'].unique()
)

df_filtered = df[df['device_name'].isin(devices)]

# ---------- Gráfico de linha ----------
st.subheader("Temperatura ao longo do tempo")
fig_line = px.line(
    df_filtered,
    x='timestamp',
    y='temperature',
    color='device_name',
    title="Temperatura por dispositivo"
)
st.plotly_chart(fig_line, use_container_width=True)

# ---------- Gráfico de barras ----------
st.subheader("Temperatura média por dispositivo")
df_mean = df_filtered.groupby('device_name')['temperature'].mean().reset_index()
fig_bar = px.bar(
    df_mean,
    x='device_name',
    y='temperature',
    title="Temperatura média"
)
st.plotly_chart(fig_bar, use_container_width=True)
