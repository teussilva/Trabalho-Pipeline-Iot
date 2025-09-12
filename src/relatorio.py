from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Cria o PDF
doc = SimpleDocTemplate("Relatorio_IoT.pdf", pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Função auxiliar para adicionar seções
def add_section(title, content):
    story.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(content, styles["Normal"]))
    story.append(Spacer(1, 24))

# ----------------- Conteúdo do relatório -----------------
intro = """Este projeto tem como objetivo demonstrar a construção de um pipeline de dados para Internet das Coisas (IoT),
focado no armazenamento e análise de leituras de temperatura. Utilizou-se PostgreSQL, Python (Pandas e SQLAlchemy) e
Streamlit para visualização dos resultados em um dashboard interativo."""

objetivo = """O objetivo do projeto foi criar:
- Um banco de dados PostgreSQL para armazenar leituras de sensores.
- Um pipeline de ingestão de dados em Python.
- Um dashboard interativo em Streamlit para análise das informações."""

metodologia = """1. Banco de Dados (PostgreSQL):
- Configurado em Docker com docker-compose.
- Tabela 'temperature_readings' para armazenar device_id, temperatura e tempo de leitura.
- Views para facilitar análises: média por dispositivo, leituras por hora, máximas/mínimas por dia.

2. Pipeline (Python + Pandas + SQLAlchemy):
- Carregamento e limpeza de dados de um arquivo CSV.
- Conversão de colunas de datas e formatação.
- Inserção automática dos dados no PostgreSQL.

3. Dashboard (Streamlit + Plotly):
- Filtros interativos por dispositivo e data.
- Gráficos: média de temperatura, leituras por hora, temperatura máxima e mínima.
- Tabela de dados filtrados."""

resultados = """O pipeline executou com sucesso a inserção de dados no banco.
O dashboard apresentou corretamente os gráficos e permitiu a interação dinâmica.
Foi comprovada a integração entre banco de dados, Python e ferramentas de visualização."""

conclusao = """O projeto alcançou o objetivo de criar um pipeline de dados IoT completo.
A integração entre PostgreSQL, Python e Streamlit mostrou-se eficaz para aplicações de monitoramento em tempo real.
O sistema pode ser expandido para incluir novos sensores e métricas."""

referencias = """- Documentação PostgreSQL
- Documentação Pandas
- Documentação Streamlit
- Materiais fornecidos na disciplina"""

# Adicionando seções
add_section("Introdução", intro)
add_section("Objetivo", objetivo)
add_section("Metodologia", metodologia)
add_section("Resultados", resultados)
add_section("Conclusão", conclusao)
add_section("Referências", referencias)

# Gera o PDF
doc.build(story)
print("✅ Relatório gerado com sucesso: Relatorio_IoT.pdf")
