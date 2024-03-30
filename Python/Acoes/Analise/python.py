import pandas as pd

pd.options.display.float_format = "{:,.2f}".format

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")

valor_max = df_principal["Variação (R$):"].max().astype(int)
valor_med = df_principal["Variação (R$):"].mean().astype(int)
valor_min = df_principal["Variação (R$):"].min().astype(int)
media_descida = df_principal[df_principal["Resultado:"] == "Subiu"] ["Variação (R$):"].mean().astype(int)
media_subida = df_principal[df_principal["Resultado:"] == "Caiu"] ["Variação (R$):"].mean().astype(int)

print(f"Máximo: {valor_max:,.2f} \nMínimo: {valor_min:,.2f} \nMédia: {valor_med:,.2f} \nMédia de descida: {media_descida:,.2f} \nMédia de subida: {media_subida:,.2f}")

df_principal_subiu = df_principal[df_principal["Resultado:"] == "Subiu"]
df_analise_segmento = df_principal_subiu.groupby("Segmento:")["Variação (R$):"].sum().reset_index()
print(df_analise_segmento)

df_analise_saldo = df_principal.groupby("Resultado:")["Variação (R$):"].sum().reset_index()
print(df_analise_saldo)