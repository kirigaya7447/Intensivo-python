import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf

#faz download dos dados do yahoo finance
dados = yf.download("PETR4.SA", start="2023-01-01", end="2024-01-01")

#coleta os dados
colunas_origin = dados.columns
#renomeia as colunas
dados.columns = ["Abertura", "Maximo", "Minimo", "Fechamento", "Ajuste de fechamento", "Volume"]

#renomeia o id
dados = dados.rename_axis("Data")
print("Dados para análise: \n", dados)

#define o intervalo de dados como sendo da coluna Fechamento e o plot faz criar a imagem e 
#define que o tamanho será de 10 X 6
dados["Fechamento"].plot(figsize=(10,6))
#dá título pro gráfico
plt.title("Variação do preço por data")
#Adiciona legenda
plt.legend("Fechamento")
#mostra o gráfico
plt.show()

#lê 60 linhas de dados e copia
df = dados.head(60).copy()
#cria coluna Data
df["Data"] = df.index
#altera o formato do Data para um compreensível para o matplotlib
df["Data"] = df["Data"].apply(mdates.date2num)
print(df)