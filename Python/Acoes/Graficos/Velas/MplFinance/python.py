import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import yfinance as yf
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

dados = yf.download("PETR4.SA", start="2023-01-01", end="2024-01-01")

mpf.plot(dados.head(30), type="candle", figsize=(10,6), volume=True, mav=(7,14), style="brasil")