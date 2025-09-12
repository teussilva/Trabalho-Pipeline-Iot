import psycopg2

# ----------------- Configuração do banco -----------------
# Aqui eu defino os parâmetros de conexão do PostgreSQL que está rodando no Docker
DB_NAME = "iot_db"
DB_USER = "postgres"
DB_PASSWORD = "12345"   # mesma senha configurada no docker-compose.yml
DB_HOST = "localhost"
DB_PORT = "5432"

# ----------------- Script SQL -----------------
# Nesse script eu removo a tabela se já existir (junto com as views que dependem dela),
# e depois recrio a tabela e as views que vou usar no dashboard
sql_script = """
-- Primeiro eu removo a tabela se já existir, junto com as dependências
DROP TABLE IF EXISTS temperature_readings CASCADE;

-- Agora recrio a tabela principal que armazena as leituras de temperatura
CREATE TABLE temperature_readings (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50),
    temperature FLOAT,
    reading_time TIMESTAMP
);

-- View que calcula a média de temperatura por dispositivo
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT 
    device_id,
    AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;

-- View que conta a quantidade de leituras por hora do dia
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT 
    EXTRACT(HOUR FROM reading_time) AS hora,
    COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- View que mostra a temperatura máxima e mínima registrada por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT 
    DATE(reading_time) AS data,
    MAX(temperature) AS temp_max,
    MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY DATE(reading_time)
ORDER BY data;
"""

# ----------------- Execução -----------------
# Aqui eu faço a conexão com o banco, executo o script e configuro tudo de uma vez
def setup_database():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute(sql_script)
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Banco recriado e configurado com sucesso!")
    except Exception as e:
        print("❌ Erro ao configurar banco:", e)


# Quando rodo esse arquivo diretamente, ele executa o setup do banco
if __name__ == "__main__":
    setup_database()

