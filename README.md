Pipeline de Dados com IoT e Docker

1. Descrição do Projeto:
   Este projeto demonstra um pipeline de dados IoT completo:
   Coleta de leituras de temperatura de dispositivos IoT.
   Armazenamento em banco de dados PostgreSQL usando Docker.
   Visualização interativa no dashboard Streamlit, com gráficos do Plotly.
   O objetivo é integrar IoT, Big Data e análise de dados de forma prática, permitindo monitoramento em tempo real e geração de insights.

2. Estrutura do Projeto
   projeto-iot/
   ├── data/
   │ ├── IOT-temp.csv # CSV original
   │ └── IOT-temp-clean.csv # CSV limpo, pronto para importação
   ├── src/
   │ └── app.py # Dashboard Streamlit
   ├── docs/
   │ └── relatorio.pdf # Relatório do projeto
   ├── docker-compose.yml # Configuração Docker
   └── README.md # Documentação do projeto

3. Configuração do Ambiente

Instale o Python (>=3.11)

Instale o Docker e Docker Compose

Crie um ambiente virtual Python:

python -m venv .venv
source .venv/bin/activate

Instale as bibliotecas necessárias:

pip install pandas psycopg2-binary sqlalchemy streamlit plotly fpdf2

4. Banco de Dados PostgreSQL com Docker Compose

Arquivo docker-compose.yml:

version: "3.9"
services:
postgres:
image: postgres:15
container_name: postgres_iot
environment:
POSTGRES_USER: postgres
POSTGRES_PASSWORD: 12345
POSTGRES_DB: iot_db
ports: - "5432:5432"
volumes: - pgdata:/var/lib/postgresql/data

volumes:
pgdata:

Rode os serviços:

docker-compose up -d

Acesse o PostgreSQL:

docker exec -it postgres_iot psql -U postgres -d iot_db

Crie a tabela:

CREATE TABLE leituras_iot (
id SERIAL PRIMARY KEY,
dispositivo VARCHAR(50),
temperatura NUMERIC,
data_hora TIMESTAMP
);

5. Importação de Dados CSV
   \copy leituras_iot(dispositivo, temperatura, data_hora)
   FROM '/caminho/absoluto/data/IOT-temp-clean.csv' DELIMITER ',' CSV HEADER;

Substitua /caminho/absoluto/data/IOT-temp-clean.csv pelo caminho correto do arquivo no seu sistema ou container.

6. Views SQL Criadas

avg_temp_por_dispositivo: média de temperatura por dispositivo.

leituras_por_hora: quantidade de leituras em cada hora do dia.

temp_max_min_por_dia: temperatura máxima e mínima por dia.

7. Dashboard Streamlit

Rode o dashboard:

streamlit run src/app.py

O dashboard apresenta:

Gráficos de tendência de temperatura por dispositivo.

Médias diárias e picos de temperatura.

Insights para monitoramento em tempo real.

8. Relatório PDF

Para gerar o relatório PDF com informações do projeto:

python gerar_relatorio.py

O PDF será salvo em: docs/relatorio.pdf

9. Comandos Git utilizados
   git init
   git add .
   git commit -m "Primeiro commit - Estrutura inicial do projeto"
   git branch -M main
   git remote add origin <URL_DO_REPOSITORIO>
   git push -u origin main

10. Observações Finais

Mantenha o CSV limpo (IOT-temp-clean.csv) para evitar erros na importação.

O projeto pode ser expandido para múltiplos sensores e dashboards mais complexos.

Com Docker Compose, basta rodar docker-compose up -d e o PostgreSQL estará pronto.
