import pandas as pd
import plotly.express as pe

pd.options.display.float_format = "{:,.2f}".format

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")

df_analise_saldo = df_principal.groupby("Resultado:")["Variação (R$):"].sum().reset_index()
print(df_analise_saldo)

grafico = pe.bar(df_analise_saldo, x="Resultado:", y="Variação (R$):", text="Variação (R$):", title="Variação X Resultado")
grafico.show()