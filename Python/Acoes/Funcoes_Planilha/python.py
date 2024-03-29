import pandas as pd

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")
df_total_acoes = pd.read_excel(planilha, sheet_name="Total_de_acoes")

pd.options.display.float_format = "{:.2f}".format

df_principal["Valor por cem"] = df_principal["Var. Dia (%)"] / 100

print(df_principal)


df_principal["Valor inicial"] = df_principal["Último (R$)"] / (1 + df_principal["Variação - dia(%):"])

print(df_principal)


df_principal = df_principal.merge(df_total_acoes, left_on="Ativo", right_on="Código", how="left")
df_principal["Qtde. Teórica"].astype(int)
print(df_principal)


df_principal = df_principal.drop(columns=["Código"])
print(df_principal)

df_principal["Var_rs"] = (df_principal["Último (R$)"] - df_principal["Valor Inicial (R$):"]) * df_principal["Qtde. Teórica"]
print(df_principal)