import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import datetime

# ----------------- Configuração do banco de dados -----------------
DB_USER = 'postgres'
DB_PASSWORD = '12345'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iot_db'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# ----------------- Configuração da página -----------------
st.set_page_config(page_title="Dashboard IoT", layout="wide")
st.title("Dashboard de Temperatura IoT")

# ----------------- Função para carregar dados -----------------
@st.cache_data
def load_data():
    query = "SELECT * FROM temperature_readings;"
    df = pd.read_sql(query, engine)
    
    # Normaliza nomes de colunas
    df.columns = df.columns.str.strip().str.lower()
    
    # Procura coluna de timestamp
    timestamp_col = None
    for col in ['timestamp', 'reading_time', 'time', 'date']:
        if col in df.columns:
            timestamp_col = col
            break
    
    if timestamp_col:
        df['timestamp'] = pd.to_datetime(df[timestamp_col])
    else:
        st.warning("Nenhuma coluna de timestamp encontrada. Criando coluna fictícia.")
        df['timestamp'] = [datetime.datetime.now() for _ in range(len(df))]
    
    return df

# ----------------- Carrega dados -----------------
df = load_data()

# ----------------- Visualização inicial -----------------
st.subheader("Visualização de dados")
st.dataframe(df.head(100))

# ----------------- Filtros -----------------
st.sidebar.header("Filtros")
devices = st.sidebar.multiselect(
    "Selecione dispositivos",
    options=df['device_id'].unique(),
    default=df['device_id'].unique()
)

df_filtered = df[df['device_id'].isin(devices)]

if df_filtered.empty:
    st.warning("Nenhum dado disponível para os dispositivos selecionados.")
else:
    # ----------------- Gráfico de linha -----------------
    st.subheader("Temperatura ao longo do tempo")
    fig_line = px.line(
        df_filtered,
        x='timestamp',
        y='temperature',
        color='device_id',
        title="Temperatura por dispositivo"
    )
    st.plotly_chart(fig_line, use_container_width=True)

    # ----------------- Gráfico de barras -----------------
    st.subheader("Temperatura média por dispositivo")
    df_mean = df_filtered.groupby('device_id')['temperature'].mean().reset_index()
    fig_bar = px.bar(
        df_mean,
        x='device_id',
        y='temperature',
        title="Temperatura média"
    )
    st.plotly_chart(fig_bar, use_container_width=True)
