import pandas as pd

pd.options.display.float_format = "{:,.2f}".format

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")

#Valor máximo da coluna Variação
valor_max = df_principal["Variação (R$):"].max().astype(int)
#Valor médio(não mediano) da coluna Variação
valor_med = df_principal["Variação (R$):"].mean().astype(int)
#Valor mínimo da coluna Variação
valor_min = df_principal["Variação (R$):"].min().astype(int)
#Média da coluna Variação quando a ação subiu, coletando a média de subida
media_descida = df_principal[df_principal["Resultado:"] == "Caiu"] ["Variação (R$):"].mean().astype(int)
#Média da coluna Variação quando a ação caiu, coletando a média de descida
media_subida = df_principal[df_principal["Resultado:"] == "Subiu"] ["Variação (R$):"].mean().astype(int)

print(f"Máximo: {valor_max:,.2f} \nMínimo: {valor_min:,.2f} \nMédia: {valor_med:,.2f} \nMédia de descida: {media_descida:,.2f} \nMédia de subida: {media_subida:,.2f}")

#coleta as linhas e colunas se a ação subiu
df_principal_subiu = df_principal[df_principal["Resultado:"] == "Subiu"]

#agrupa com base no segmento das empresas e soma os valores de Variação
df_analise_segmento = df_principal_subiu.groupby("Segmento:")["Variação (R$):"].sum().reset_index()
print(df_analise_segmento)

#agrupa com base no resultado das empresas e soma os valores de Variação
df_analise_saldo = df_principal.groupby("Resultado:")["Variação (R$):"].sum().reset_index()
print(df_analise_saldo)