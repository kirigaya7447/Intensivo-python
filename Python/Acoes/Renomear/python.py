import pandas as pd

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")

#realiza uma cópia apenas das colunas apresentadas
df_principal = df_principal[["Ativo", "Data", "Último (R$)", "Var. Dia (%)"]].copy()

print("Colunas cruas: \n", df_principal)

#renomeia as colunas e copia
df_principal = df_principal.rename(columns={"Último (R$)": "Ultimo(R$)", "Var. Dia (%)": "Var_Dia(%)"}).copy()

print("Colunas renomeadas: \n", df_principal)