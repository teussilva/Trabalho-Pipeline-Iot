import pandas as pd
from sqlalchemy import create_engine, text

# ----------------- Configuração do banco de dados -----------------
DB_USER = 'postgres'
DB_PASSWORD = '12345'  # mesma senha que você usou no docker-compose.yml
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'iot_db'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# ----------------- Carregar CSV -----------------
csv_path = "data/IOT-temp-clean.csv"
print(f"📂 Lendo arquivo CSV em: {csv_path}")

df = pd.read_csv(csv_path)
print(f"🔎 Colunas encontradas: {list(df.columns)}")

# Renomear colunas para ficar igual às da tabela do banco
df = df.rename(columns={
    "room_id/id": "device_id",
    "noted_date": "reading_time",
    "temp": "temperature",
    "out/in": "location"
})

# Garantir que a coluna de tempo esteja no formato datetime
df['reading_time'] = pd.to_datetime(df['reading_time'], errors='coerce')

# ----------------- Inserir no Banco -----------------
print("💾 Limpando dados antigos...")
with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE temperature_readings;"))

print("💾 Inserindo novos dados no PostgreSQL...")
df[['device_id', 'temperature', 'reading_time']].to_sql(
    "temperature_readings",
    engine,
    if_exists="append",
    index=False
)

print("✅ Dados inseridos com sucesso!")

