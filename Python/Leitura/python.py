import pandas as pd

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")
print(df_principal.head(5))

df_acoes = pd.read_excel(planilha, sheet_name="Total_de_acoes")
print(df_acoes.head(7))

df_ticker = pd.read_excel(planilha, sheet_name="Ticker")
print(df_ticker)