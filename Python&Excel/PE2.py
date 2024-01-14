import pandas as pd

tabela =pd.read_excel("ExcelExemplo.xlsx")



import plotly.express as px
grafico = px.pie(tabela, names="Trabalho", title="Distribuição de Trabalhos", hole=0.3)
grafico.show()