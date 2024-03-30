import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from prophet import Prophet

dados = yf.download("JNJ", start="2020-01-01", end="2023-12-31", progress=True)
dados = dados.reset_index()

dados_treino = dados[dados["Date"] < "2023-07-31"]
dados_teste = dados[dados["Date"] >= "2023-07-31"]

print(dados, dados_teste, dados_treino)

dados_prophet_treino = dados_treino[["Date", "Close"]].rename(columns={"Date": "ds", "Close": "y"})

print(dados_prophet_treino)

model = Prophet(weekly_seasonality=True,
                 yearly_seasonality=True,
                 daily_seasonality=False)

model.add_country_holidays(country_name="US")

model.fit(dados_prophet_treino)

future = model.make_future_dataframe(periods=150)
previsao = model.predict(future)

print (previsao)

plt.figure(figsize=(8,8))
plt.plot(dados_treino["Date"], dados_treino["Close"], label="Dados de Treino", color="red")
plt.plot(dados_teste["Date"], dados_teste["Close"], label="Dados de Teste", color="green")
plt.plot(previsao["ds"], previsao["yhat"], label="Dados do profeta", color="blue", linestyle="--")

plt.axvline(dados_treino["Date"].max(), color="yellow", linestyle="--", label="Início da previsão")
plt.xlabel("Data")
plt.ylabel("Valor do fechamento")
plt.title("Previsão do fechamento X Dados reais")
plt.legend()
plt.show()