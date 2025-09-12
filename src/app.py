import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ----------------- Conexão com o banco -----------------
# Aqui faço a conexão com o PostgreSQL que está rodando no Docker
DB_USER = 'postgres'
DB_PASSWORD = '12345'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iot_db'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# ----------------- Configuração da página -----------------
# Ajusto as configurações da página no Streamlit
st.set_page_config(page_title="Dashboard IoT", layout="wide")
st.title("Dashboard de Temperatura IoT")

# ----------------- Função para carregar dados -----------------
# Criei essa função pra buscar dados do banco com cache,
# assim não fica repetindo a query toda hora
@st.cache_data
def load_data(query):
    return pd.read_sql(query, engine)

# ----------------- Carregando os dados -----------------
# Pego todos os dados crus da tabela principal
df_full = load_data("SELECT * FROM temperature_readings;")

# ----------------- Tratamento da coluna de tempo -----------------
# Converto pra datetime e removo valores nulos pra não dar erro nos filtros
df_full['reading_time'] = pd.to_datetime(df_full['reading_time'], errors='coerce')
df_full = df_full.dropna(subset=['reading_time'])

# ----------------- Barra lateral - Filtros -----------------
st.sidebar.header("Filtros")

# Filtro de dispositivos
devices = st.sidebar.multiselect(
    "Selecione dispositivos",
    options=df_full['device_id'].unique(),
    default=df_full['device_id'].unique()
)

# Filtro de datas (garantindo que sempre exista intervalo válido)
if not df_full.empty:
    min_date = df_full['reading_time'].min().date()
    max_date = df_full['reading_time'].max().date()
else:
    min_date = max_date = pd.Timestamp.today().date()

date_range = st.sidebar.date_input(
    "Selecione intervalo de datas",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Tratamento pra garantir que sempre tem início e fim
if isinstance(date_range, list) and len(date_range) == 2:
    start_date, end_date = date_range
elif isinstance(date_range, list) and len(date_range) == 1:
    start_date = end_date = date_range[0]
else:
    start_date, end_date = min_date, max_date

# Aplicando os filtros
df_filtered = df_full[
    (df_full['device_id'].isin(devices)) &
    (df_full['reading_time'].dt.date >= start_date) &
    (df_full['reading_time'].dt.date <= end_date)
]

# ----------------- Gráfico 1: Média de Temperatura -----------------
# Aqui mostro a média de temperatura por dispositivo
st.subheader("Média de temperatura por dispositivo")
df_avg_temp = df_filtered.groupby("device_id")["temperature"].mean().reset_index()
fig_avg = px.bar(
    df_avg_temp,
    x='device_id',
    y='temperature',
    title="Média de Temperatura por Dispositivo",
    labels={'device_id': 'Dispositivo', 'temperature': 'Temperatura Média'}
)
st.plotly_chart(fig_avg, use_container_width=True)

# ----------------- Gráfico 2: Leituras por Hora -----------------
# Faço a contagem de leituras agrupadas por hora do dia
st.subheader("Contagem de leituras por hora do dia")
df_filtered["hora"] = df_filtered["reading_time"].dt.hour
df_leituras_hora = df_filtered.groupby("hora")["id"].count().reset_index()
df_leituras_hora.rename(columns={"id": "contagem"}, inplace=True)

fig_hour = px.bar(
    df_leituras_hora,
    x='hora',
    y='contagem',
    title="Leituras por hora",
    labels={'hora': 'Hora do dia', 'contagem': 'Quantidade de leituras'}
)
st.plotly_chart(fig_hour, use_container_width=True)

# ----------------- Gráfico 3: Temperatura Máx/Min -----------------
# Aqui mostro a máxima e mínima por dia
st.subheader("Temperatura máxima e mínima por dia")
df_temp_dia = df_filtered.groupby(df_filtered["reading_time"].dt.date)["temperature"].agg(
    temp_max="max", temp_min="min"
).reset_index().rename(columns={"reading_time": "data"})

fig_temp = px.line(
    df_temp_dia,
    x='data', 
    y=['temp_max', 'temp_min'],
    title="Temperatura Máx/Min por dia",
    labels={'data': 'Data', 'value': 'Temperatura', 'variable': 'Métrica'}
)
st.plotly_chart(fig_temp, use_container_width=True)

# ----------------- Tabela -----------------
# No final mostro uma amostra dos dados filtrados
st.subheader("Visualização de dados filtrados")
st.dataframe(df_filtered.head(100))

