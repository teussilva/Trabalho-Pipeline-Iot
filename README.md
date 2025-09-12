# Pipeline de Dados com IoT e Docker

## 1. Descrição do Projeto

Este projeto demonstra um pipeline de dados IoT completo:

- Coleta de leituras de temperatura de dispositivos IoT.
- Armazenamento em banco de dados PostgreSQL usando Docker.
- Visualização interativa no dashboard **Streamlit**, com gráficos feitos no **Plotly**.
- O objetivo é integrar IoT, Big Data e análise de dados de forma prática, permitindo monitoramento
  em tempo real e geração de insights.

## 2. Estrutura do Projeto

Trabalho-Pipeline-IoT/
├── data/
│ ├── IOT-temp.csv # CSV original
│ └── IOT-temp-clean.csv # CSV limpo, pronto para importação
├── docs/
│ ├── relatorio_modelo.pdf # Modelo de relatório fornecido
│ └── relatorio.pdf # Relatório teórico final
├── sql/
│ ├── create_tables.sql # Script de criação das tabelas
│ └── views.sql # Criação das views analíticas
├── src/
│ ├── app.py # Dashboard Streamlit
│ ├── pipeline.py # Pipeline de ingestão de dados
│ ├── relatorio.py # Script de geração automática de relatório
│ ├── setup_db.py # Script de configuração inicial do banco
│ └── test.py # Testes de leitura de CSV
├── .gitignore # Arquivos a serem ignorados pelo Git
├── docker-compose.yml # Configuração do Docker PostgreSQL
├── gerar_relatorio.py # Alternativa para geração de relatórios
├── README.md # Documentação do projeto
├── Relatorio_IoT.pdf # Exportação final em PDF do relatório
└── requirements.txt # Lista de dependências do projeto

## 3. Configuração do Ambiente

1. Instale o **Python (>=3.11)**
2. Instale o **Docker e Docker Compose**
3. Crie um ambiente virtual Python:
   python -m venv .venv

# Windows

.venv\Scripts\activate

# Linux / Mac

source .venv/bin/activate 4. Instale as bibliotecas necessárias:
pip install pandas psycopg2-binary sqlalchemy streamlit plotly

## 4. Banco de Dados com Docker

Arquivo **docker-compose.yml**:
services:
postgres-iot:
image: postgres:15
container_name: postgres-iot
environment:
POSTGRES_USER: postgres
POSTGRES_PASSWORD: 12345
POSTGRES_DB: iot_db
ports:

- "5432:5432"
  volumes:
- pgdata:/var/lib/postgresql/data
  volumes:
  pgdata:
  Subir o container:
  docker-compose up -d
  Acessar o PostgreSQL:
  docker exec -it postgres-iot psql -U postgres -d iot_db
  Executar scripts SQL:
  \i sql/create_tables.sql
  \i sql/views.sql
  Importar dados:
  \copy temperature_readings(device_id, temperature, reading_time)
  FROM '/caminho/absoluto/data/IOT-temp-clean.csv' DELIMITER ',' CSV HEADER;
  ■■ Substitua `/caminho/absoluto/...` pelo caminho correto no seu sistema ou container.

## 5. Views SQL Criadas

- **avg_temp_por_dispositivo** → média de temperatura por dispositivo.
- **leituras_por_hora** → quantidade de leituras em cada hora do dia.
- **temp_max_min_por_dia** → temperatura máxima e mínima por dia.

## 6. Dashboard Streamlit

Rodar o dashboard:
streamlit run src/app.py
O dashboard apresenta:

- Gráficos de média de temperatura por dispositivo.
- Contagem de leituras por hora.
- Temperatura máxima e mínima por dia.

## 7. Prints do Dashboard

Média de Temperatura por Dispositivo
Contagem de Leituras por Hora do Dia
Temperatura Máxima e Mínima por Dia

## 8. Referências

- [Kaggle
  Dataset](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices)
- [Docker Docs](https://docs.docker.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)

## 9. Autor

Projeto desenvolvido por [Matheus Henrique Alves da Silva] para a disciplina Disruptive Architectures: IoT, Big Data e IA.
