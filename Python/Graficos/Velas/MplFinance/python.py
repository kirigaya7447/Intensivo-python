import mplfinance as mpf
import yfinance as yf

#download dos dados
dados = yf.download("PETR4.SA", start="2023-01-01", end="2024-01-01")
dados_apple = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

#cria gráfico com a api do tipo candle, define tamanho. Volume é um segundo gráfico de 
#barras que verifica o volume. O mav é a média móvel que é de 7 e 14 dias
#e o style é apenas cor
mpf.plot(dados.head(90), type="candle", figsize=(10,6), volume=True, mav=(7, 14), style="brasil")

mpf.plot(dados.head(360), type="line", figsize=(10,6), volume=True, mav=(7, 14, 30), style="yahoo")

mpf.plot(dados_apple.head(180), type="candle", figsize=(10,6), volume=True, mav=(30), style="yahoo")