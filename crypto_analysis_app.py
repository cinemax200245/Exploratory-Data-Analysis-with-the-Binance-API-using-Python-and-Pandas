import streamlit as st
import pandas as pd
import plotly.express as px
import cufflinks as cf
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

apiKey = 'S9qqbQoL7OYrDi6CqVKmIhitVItgYwbi6TIVtf3Pni2dM4eHt1wTjM4OZLgW1yt5'
secretKey = '2bGRDM3SQNLWDlhXvsQcD8rbNxH3Aolx3SbZn2lvtniNDAVMIPxmPFMYYZoAaeVF'

#client = Client(apiKey, secretKey)

def fetch_crypto_data(crypto_symbol, interval='1d', start_date='2011-01-01'):
    try:
        # Create the Binance client
        client = Client(apiKey, secretKey)

        # Fetch historical data
        historical = client.get_historical_klines(crypto_symbol, interval, start_date)
        
        if historical is None:
            st.warning(f"Data not available for {crypto_symbol}. Please check the cryptocurrency symbol.")
            return pd.DataFrame()

        # Process the data
        historicalDf = pd.DataFrame(historical)
        historicalDf.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 
                                'Volume', 'Close Time', 'Quote Asset Volume', 'Number of Trades', 
                                'Taker Buy Base Volume', 'Taker Buy Quote Volume', 'Ignore']
        historicalDf['Open Time'] = pd.to_datetime(historicalDf['Open Time']/1000, unit='s')
        historicalDf['Close Time'] = pd.to_datetime(historicalDf['Close Time']/1000, unit='s')
        numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume',
                        'Quote Asset Volume', 'Taker Buy Base Volume',
                        'Taker Buy Quote Volume']
        historicalDf[numeric_cols] = historicalDf[numeric_cols].apply(pd.to_numeric, axis=1)
        return historicalDf
    
    except Exception as e:
        st.warning(f"An error occurred: {str(e)}")
        return pd.DataFrame()

def plot_candlestick_chart(data):
    fig = px.candlestick(data, x='Open Time', open='Open', high='High', low='Low', close='Close', title='Candlestick Chart')
    st.plotly_chart(fig)

def plot_monthly_average_price(data):
    monthly_prices = data.resample('M').mean().reset_index()
    fig = px.scatter(monthly_prices, x='Open Time', y='Close', trendline='ols', title='Monthly Average Closing Price')
    st.plotly_chart(fig)

def plot_monthly_price_distribution(data):
    monthly_prices = data.resample('M').mean().reset_index()
    monthly_prices.iplot(kind='box', x='Open Time', y='Close', title='Monthly Closing Price Distribution')

def main():
    st.title("Cryptocurrency Price Analysis App")

    # User input for cryptocurrency symbol
    crypto_symbol = st.text_input("Enter the symbol of the cryptocurrency (e.g., BTCUSDT):", "BTCUSDT")

    # Fetch historical data for the specified cryptocurrency
    crypto_data = fetch_crypto_data(crypto_symbol)

    if not crypto_data.empty:
        st.header(f"Analysis for {crypto_symbol}")

        # Plot Candlestick Chart
        st.subheader("Candlestick Chart")
        plot_candlestick_chart(crypto_data)

        # Plot Monthly Average Closing Price
        st.subheader("Monthly Average Closing Price")
        plot_monthly_average_price(crypto_data)

        # Plot Monthly Closing Price Distribution
        st.subheader("Monthly Closing Price Distribution")
        plot_monthly_price_distribution(crypto_data)

if __name__ == "__main__":
    main()
