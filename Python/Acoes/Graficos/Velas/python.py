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

figura, ax = plt.subplots(figsize=(10, 6))
width = 0.7

for cont in range(len(df)):
    if df["Fechamento"].iloc[cont] > df["Abertura"].iloc[cont]:
        color = "green"
    else:
        color = "red"

    ax.plot([df["Data"].iloc[cont], df["Data"].iloc[cont]],
            [df["Minimo"].iloc[cont], df["Maximo"].iloc[cont]],
            color= color,
            linewidth=1)
    
    ax.add_patch(plt.Rectangle((df["Data"].iloc[cont] - width/2, min(df["Abertura"].iloc[cont], df["Fechamento"].iloc[cont])),
                               width,
                               abs(df["Fechamento"].iloc[cont] - df["Abertura"].iloc[cont]),
                               facecolor=color))

df["MA7"] = df["Fechamento"].rolling(window=7).mean()    
df["MA14"] = df["Fechamento"].rolling(window=14).mean()

ax.plot(df["Data"], df["MA7"], color="blue", label="Média móvel de 7 dias")
ax.plot(df["Data"], df["MA14"], color="pink", label="Média móvel de 14 dias")
ax.legend()

ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=60)

plt.title("Meu Gráfico")
plt.xlabel("Data")
plt.ylabel("Valor")

plt.grid(True)

plt.show()

figu = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                     vertical_spacing=0.1, subplot_titles=("Candlesticks", "Volume Transacionado"), 
                     row_width=[0.2, 0.7])

figu.add_trace(go.Candlestick(x=df.index, 
                              open=df["Abertura"], 
                              close=df["Fechamento"],
                              high=df["Maximo"],
                              low=df["Minimo"],
                              name="Candlestick"),
                              row= 1, col= 1)

figu.add_trace(go.Scatter(x=df.index,
                          y=df["MA7"],
                          mode="lines",
                          name="MA7 - Média móvel de 7 dias"),
                          row=1, col=1)

figu.add_trace(go.Scatter(x=df.index,
                          y=df["MA14"],
                          mode="lines",
                          name="MA14 - Média móvel de 14 dias"),
                          row=1, col=1)

figu.add_trace(go.Bar(x=df.index,
                      y=df["Volume"],
                      name="Volume"), 
                      row=2, col=1)

figu.update_layout(yaxis_title="Preço",
                   xaxis_rangeslider_visible=False,
                   width=1100, height=600)

figu.show()

dados.columns = colunas_origin
mpf.plot(dados.head(30), type="candle", figsize=(10,6), volume=True, mav=(7,14), style="brasil")
