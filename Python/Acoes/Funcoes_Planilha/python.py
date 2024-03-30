import pandas as pd

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")
df_total_acoes = pd.read_excel(planilha, sheet_name="Total_de_acoes")
df_ticker = pd.read_excel(planilha, sheet_name="Ticker")
df_chat = pd.read_excel(planilha, sheet_name="ChatGPT")

pd.options.display.float_format = "{:,.2f}".format

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

df_principal["Resultado"] = df_principal["Variação (R$):"].apply(lambda cont: "Subiu" if cont > 0 else("Manteve" if cont == 0 else("Caiu")))
print(df_principal)

df_principal = df_principal.merge(df_ticker, left_on="Ativo", right_on="Ticker", how="left")
df_principal = df_principal.rename(columns={"Nome": "Nome_da_empresa"}).copy()
df_principal = df_principal.drop(columns=["Ticker"])
print(df_principal)

df_principal = df_principal.merge(df_chat, left_on="Nome_da_empresa", right_on="Empresa:", how="left")
df_principal = df_principal.drop(columns=["Empresa:"])
df_principal = df_principal.rename(columns={"Segmento:_y" : "Segmento", "Idade (anos):": "Idade(anos)"})
print(df_principal)

df_principal["Categoria_idade"] = df_principal["Idade(anos)"].apply(lambda cont: "Mais de 100 anos" if cont > 100 else("Menos de 50 anos" if cont < 50 else("Entre 50 e 100 anos")))
print(df_principal)