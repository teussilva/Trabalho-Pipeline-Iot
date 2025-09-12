-- -----------------------------
-- Views do banco IoT
-- -----------------------------

-- Contagem de leituras por hora do dia
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT 
    EXTRACT(HOUR FROM reading_time) AS hora,
    COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- Temperaturas máximas e mínimas por dia
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT 
    DATE(reading_time) AS data,
    MAX(temperature) AS temp_max,
    MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY data
ORDER BY data;

-- Média de temperatura por dispositivo
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT 
    device_id,
    AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id
ORDER BY device_id;
