-- -----------------------------
-- Tabelas do banco IoT
-- -----------------------------

-- Tabela de leituras de temperatura
CREATE TABLE IF NOT EXISTS temperature_readings (
    id SERIAL PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,
    temperature NUMERIC(5,2) NOT NULL,
    reading_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
