import pandas as pd
import plotly.express as pe

pd.options.display.float_format = "{:,.2f}".format

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")

#agrupa por Resultado e soma a variação
df_analise_saldo = df_principal.groupby("Resultado:")["Variação (R$):"].sum().reset_index()
print("Tabela com a somatória de descida e subida: \n", df_analise_saldo)

grafico = pe.bar(df_analise_saldo, x="Resultado:", y="Variação (R$):", text="Variação (R$):", title="Variação X Resultado")
grafico.show()

#conta quantas empresas tem mais de 100 anos
mais_de_cem = df_principal["Categoria de idade:"].value_counts()["Mais de 100 anos"]
#conta quantas empresas tem menos de 50 anos
menos_de_cinquenta = df_principal["Categoria de idade:"].value_counts()["Menos de 50 anos"]
#conta quantas empresas tem entre 50 e 100 anos
entre = df_principal["Categoria de idade:"].value_counts()["Empresa de 50 a 100 anos"]
#cria um dataframe com os valores acima
coluna_idade = pd.DataFrame([["Empresas com mais de 100 anos", mais_de_cem], ["Empresas com menos de 50 anos", menos_de_cinquenta], ["Empresas entre os 50 e 100 anos", entre]], columns=["Variacao","Idade"])
#configura e formata o grafico
grafico_idade = pe.bar(coluna_idade, y="Idade", x="Variacao", title="Idade de empresas")
grafico_idade.show()