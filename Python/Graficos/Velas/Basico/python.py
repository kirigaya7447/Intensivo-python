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
print(dados)

dados["Fechamento"].plot(figsize=(10,6))
plt.title("Variação do preço por data")
plt.legend("Fechamento")

plt.show()

df = dados.head(60).copy()
df["Data"] = df.index
df["Data"] = df["Data"].apply(mdates.date2num)
print(df)