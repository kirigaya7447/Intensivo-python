import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

dados = yf.download("PETR4.SA", start="2023-01-01", end="2024-01-01")
colunas_origin = dados.columns
dados.columns = ["Abertura", "Maximo", "Minimo", "Fechamento", "Ajuste de fechamento", "Volume"]
dados = dados.rename_axis("Data")
print(dados)

dados["Fechamento"].plot(figsize=(10, 6))
plt.title("variação do preço por data")
plt.legend("Fechamento")

plt.show()

df = dados.head(60).copy()
df["Data"] = df.index
df["Data"] = df["Data"].apply(mdates.date2num)
print(df)