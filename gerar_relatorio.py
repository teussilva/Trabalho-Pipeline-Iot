from fpdf import FPDF
import os

# Caminho de saída do PDF
output_dir = "docs"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_file = os.path.join(output_dir, "relatorio.pdf")

# Criação do PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# Título
pdf.cell(0, 10, "Projeto Pipeline de Dados IoT", ln=True, align="C")
pdf.ln(10)

# Seções
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "1. Contextualização do Projeto", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 8,
    "Este projeto tem como objetivo criar um pipeline de dados que processa leituras "
    "de temperatura de dispositivos IoT, armazenando-os em um banco de dados PostgreSQL "
    "utilizando Docker. Os dados são processados e visualizados em um dashboard Streamlit."
)
pdf.ln(5)

pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "2. Passos Realizados", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 8,
    "- Configuração do ambiente Python e instalação de dependências.\n"
    "- Criação do container PostgreSQL com Docker.\n"
    "- Inserção dos dados CSV limpos no banco de dados.\n"
    "- Criação de 3 views SQL para análises específicas.\n"
    "- Construção do dashboard em Streamlit com gráficos interativos."
)
pdf.ln(5)

pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "3. Views SQL Criadas", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 8,
    "1) avg_temp_por_dispositivo: mostra a média de temperatura por dispositivo.\n"
    "2) leituras_por_hora: contabiliza a quantidade de leituras em cada hora do dia.\n"
    "3) temp_max_min_por_dia: exibe a temperatura máxima e mínima por dia."
)
pdf.ln(5)

pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "4. Prints do Dashboard", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 8,
    "Os gráficos interativos do Streamlit mostram tendências, picos e médias das "
    "temperaturas registradas pelos dispositivos IoT. (Inclua capturas de tela se possível)"
)
pdf.ln(5)

pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, "5. Insights e Uso Prático", ln=True)
pdf.set_font("Arial", '', 11)
pdf.multi_cell(0, 8,
    "Com os dados coletados, é possível monitorar condições críticas de temperatura, "
    "prevenir falhas em equipamentos e otimizar processos em ambientes reais de IoT."
)

# Salva o PDF
#pdf.output(output_file, encoding="utf-8")
print(f"PDF gerado com sucesso: {output_file}")
