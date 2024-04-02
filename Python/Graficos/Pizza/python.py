import pandas as pd
import plotly.express as pe

pd.options.display.float_format = "{:,.2f}".format

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_chat = pd.read_excel(planilha, sheet_name="ChatGPT")
print(df_chat)

df_idade = df_chat.groupby(["Idade (anos):"]).sum().reset_index()
df_idade = df_idade.drop(columns=["Empresa:"])
df_idade = df_idade.drop(columns=["Segmento:"])
df_idade["index"] = df_idade.index
print(df_idade)


grafico = pe.pie(values=df_idade["Idade (anos):"], names=df_idade["index"], title="Hello!")
grafico.show()