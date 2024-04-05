import pandas as pd

planilha = "/home/joao4774/Área de Trabalho/GitHub/Intensivo-python/Planilha/Planilha.xlsx"

df_principal = pd.read_excel(planilha, sheet_name="Principal")
df_total_acoes = pd.read_excel(planilha, sheet_name="Total_de_acoes")
df_ticker = pd.read_excel(planilha, sheet_name="Ticker")
df_chat = pd.read_excel(planilha, sheet_name="ChatGPT")

pd.options.display.float_format = "{:,.2f}".format

#divide o Var Dia por 100
df_principal["Valor por cem"] = df_principal["Var. Dia (%)"] / 100

print("Var dia /100: ", df_principal)

#divide o valor do final do dia da ação pela soma de Variação e 1
df_principal["Valor inicial"] = df_principal["Último (R$)"] / (1 + df_principal["Variação - dia(%):"])

print("Valor inicial da ação:", df_principal)


#mesclagem das tabelas Principal e Total_acoes com base no nome da ação
df_principal = df_principal.merge(df_total_acoes, left_on="Ativo", right_on="Código", how="left")
#agora que as tabelas estão mescladas, converte o quantitade teórica para int
df_principal["Qtde. Teórica"].astype(int)
print("Mesclagem de Principal e Total_Acoes: ", df_principal)

#retira a coluna Código
df_principal = df_principal.drop(columns=["Código"])
print("Tirado a coluna código:", df_principal)

#Obtendo a variação através da subtração do valor final da ação no dia pela inicial e depois multiplicado pela quantidade teórica
df_principal["Var_rs"] = (df_principal["Último (R$)"] - df_principal["Valor inicial"]) * df_principal["Qtde. Teórica"]
print("Variação do dia: ", df_principal)

#através da coluna Variação se aplica uma chamada de código, e nele se cria uma variável cont para verificar cada linha da coluna,
#ao decorrer das linhas usa-se um operador ternário para verificar se a ação subiu, estagnou ou caiu 
df_principal["Resultado"] = df_principal["Variação (R$):"].apply(lambda cont: "Subiu" if cont > 0 else("Manteve" if cont == 0 else("Caiu")))
print("O que aconteceu com a ação: ", df_principal)

#juntam-se as tabelas Principal e Ticker
df_principal = df_principal.merge(df_ticker, left_on="Ativo", right_on="Ticker", how="left")
#renomeia a coluna Nome para Nome_da_empresa
df_principal = df_principal.rename(columns={"Nome": "Nome_da_empresa"}).copy()
#apaga a coluna ticker
df_principal = df_principal.drop(columns=["Ticker"])
print("Coleta do nome da empresa: ", df_principal)

#realiza-se um merge entre o Principal e a coluna do CHATGPT
df_principal = df_principal.merge(df_chat, left_on="Nome_da_empresa", right_on="Empresa:", how="left")
#retira a coluna que tem o nome da empresa para não ter repetição
df_principal = df_principal.drop(columns=["Empresa:"])
#renomeiam as colunas: Segmento:_y e Idade (anos), para Segmento e Idades(anos) 
df_principal = df_principal.rename(columns={"Segmento:_y" : "Segmento", "Idade (anos):": "Idade(anos)"})
print("Coletando o segmento e idade das empresas: ", df_principal)

#através de uma chamada de código utilizando o Idade, verifica, através de operador ternário, se a empresa tem mais, menos ou até 100 anos
df_principal["Categoria_idade"] = df_principal["Idade(anos)"].apply(lambda cont: "Mais de 100 anos" if cont > 100 else("Menos de 50 anos" if cont < 50 else("Entre 50 e 100 anos")))
print("Catalogando as idades: ", df_principal)