from flask import Flask, render_template
import requests
import pandas as pd
import numpy as np
import ta

app = Flask(__name__)

# Alpha Vantage API key
api_key = 'FNNCSTNXIBBFC4L1'

def fetch_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=csv'
    df = pd.read_csv(url)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    return df

def generate_signals(df):
    df['SMA50'] = ta.trend.sma_indicator(df['close'], window=50)
    df['SMA200'] = ta.trend.sma_indicator(df['close'], window=200)
    df['signal'] = 0
    df['signal'][50:] = np.where(df['SMA50'][50:] > df['SMA200'][50:], 1, 0)
    df['position'] = df['signal'].diff()
    return df

@app.route('/')
def index():
    symbol = 'NEPSE'
    df = fetch_data(symbol)
    df = generate_signals(df)
    signals = df[df['position'].notnull()]
    return render_template('index.html', signals=signals.to_html())

if __name__ == '__main__':
    app.run(debug=True)
