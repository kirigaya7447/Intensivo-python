import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import yfinance as yf

#faz download dos dados
dados = yf.download("PETR4.SA", start="2023-01-01", end="2024-01-01")
#coleta os dados
colunas_origin = dados.columns
#renomeia as colunas
dados.columns = ["Abertura", "Maximo", "Minimo", "Fechamento", "Ajuste de fechamento", "Volume"]
#renomeia o id
dados = dados.rename_axis("Data")
print("Dados formatados: \n", dados)

#lê as primeiras 60 linhas e copia
df = dados.head(60).copy()
#cria o Data 
df["Data"] = df.index
#transforma o Data para um formato que matplot entenda
df["Data"] = df["Data"].apply(mdates.date2num)
print("Data formatado: \n", df)

#cria a figura e o eixo com o tamanho especificado
figura, ax = plt.subplots(figsize=(10, 6))
#define a largura
width = 0.5

#itera pegando cada linha
for cont in range(len(df)):
    #define a cor com base se subiu ou caiu a ação
    if df["Fechamento"].iloc[cont] > df["Abertura"].iloc[cont]:
        color = "green"
    else:
        color = "red"

    #plota uma linha vertical com x e y definidos, no caso de y ele vai do Minimo até o Máximo
    ax.plot([df["Data"].iloc[cont], df["Data"].iloc[cont]], [df["Minimo"].iloc[cont], df["Maximo"].iloc[cont]],
            color= color,
            linewidth=1)
    
    #adiciona o retângulo como "corpo" da ação
    ax.add_patch(plt.Rectangle((df["Data"].iloc[cont] - width/2, min(df["Abertura"].iloc[cont], df["Fechamento"].iloc[cont])),
                               width,
                               abs(df["Fechamento"].iloc[cont] - df["Abertura"].iloc[cont]),
                               facecolor=color))

#em um intervalo de 7 dias(espaços) coleta a média entre eles
df["MA7"] = df["Fechamento"].rolling(window=7).mean()    
#em um intervalo de 14 dias(espaços) coleta a média entre eles
df["MA14"] = df["Fechamento"].rolling(window=14).mean()

#adiciona as médias móveis no gráfico
ax.plot(df["Data"], df["MA7"], color="blue", label="Média móvel de 7 dias")
ax.plot(df["Data"], df["MA14"], color="pink", label="Média móvel de 14 dias")
#adiciona uma legenda, que será o label dos dados 
ax.legend()

#modificxa as datas para um formato estadunidense
ax.xaxis_date()
#formata o x para o nosso formato
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
#define a rotação apenas para deixa mais legível
plt.xticks(rotation=60)

#título
plt.title("Meu Gráfico")
#define o título de x
plt.xlabel("Data")
#define o título de y
plt.ylabel("Valor")
#coloca grade
plt.grid(True)
#mostra o resultado
plt.show()