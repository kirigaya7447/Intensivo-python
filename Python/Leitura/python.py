import pandas as pd

df_principal = pd.read_excel("/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx", sheet_name="Principal")
print(df_principal.head(5))

df_acoes = pd.read_excel("/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx", sheet_name="Total_de_acoes")
print(df_acoes.head(7))

df_ticker = pd.read_excel("/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx", sheet_name="Ticker")
print(df_ticker)