import yfinance as yf
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

#download das datas da ação
dados = yf.download("PETR4.SA", start="2023-01-01", end="2024-01-01")
#armazenamento de dados
colunas_origin = dados.columns
#renomeia as colunas
dados.columns = ["Abertura", "Maximo", "Minimo", "Fechamento", "Ajuste de fechamento", "Volume"]
print("Dados formatados: \n", dados)

#copia as primeiras 60 linhas para um DataFrame
df = dados.head(180).copy()

#média de 7 linhas(dias)
df["MA7"] = df["Fechamento"].rolling(window=7).mean()    
#média de 14 linhas(dias)
df["MA14"] = df["Fechamento"].rolling(window=14).mean()

#cria espaço para gráfico definindo linhas, colunas e tamanho das linhas
figu = make_subplots(rows=3, cols=1, shared_xaxes=False, 
                     vertical_spacing=0.1, subplot_titles=("Candlesticks", "Volume Transacionado", "Fechamento"), 
                     row_width=[1, 1, 1])

#cria linha no estilo de vela para mostrar as ações
figu.add_trace(go.Candlestick(x=df.index, 
                              open=df["Abertura"], 
                              close=df["Fechamento"],
                              high=df["Maximo"],
                              low=df["Minimo"],
                              name="Ação"),
                              row=1, col=1)

#cria linha para mostrar a média de 7 dias
figu.add_trace(go.Scatter(x=df.index,
                          y=df["MA7"],
                          mode="lines",
                          name="MA7 - Média móvel de 7 dias"),
                          row=1, col=1)

#cria linha para mostrar a média de 14 dias
figu.add_trace(go.Scatter(x=df.index,
                          y=df["MA14"],
                          mode="lines",
                          name="MA14 - Média móvel de 14 dias"),
                          row=1, col=1)

#cria a tabela de barras na segunda linha, contendo informações do volume das ações
figu.add_trace(go.Bar(x=df.index,
                      y=df["Volume"],
                      name="Volume"), 
                      row=2, col=1)


#cria mais uma tabela de barras, só que na terceira linha e com o fechamento das ações
figu.add_trace(go.Bar(x=df.index,
                      y=df["Fechamento"],
                      name="Fechamento"), 
                      row=3, col=1)

#atualiza o gráfico e coloca o título do y como Preço, oculta a linha do volume e 
#define altura e largura
figu.update_layout(yaxis_title="Preço",
                   xaxis_rangeslider_visible=False,
                   width=1800, height=1500)

figu.show()