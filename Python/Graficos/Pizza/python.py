import pandas as pd
import plotly.express as pe

pd.options.display.float_format = "{:,.2f}".format

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")

df_analise = df_principal["Segmento:"]
df_analise = pd.concat([df_analise, df_principal["Variação (R$):"]], axis=1)
df_analise = pd.concat([df_analise, df_principal["Resultado:"]], axis=1)


df_analise = df_analise.groupby("Segmento:")["Variação (R$):"].sum().reset_index()
df_analise["Variação (R$):"] = df_analise["Variação (R$):"].apply(lambda cont: cont * -1 if cont < 0 else(cont * 1))

print("Dados a serem analisados: \n", df_analise)

grafico = pe.pie(values=df_analise["Variação (R$):"], names=df_analise["Segmento:"], title="Segmentos e suas respectivas ações:")
grafico.show()