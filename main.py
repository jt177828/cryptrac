import yfinance as yf
import streamlit as st

st.write(
'''
# Cryptrac
'''
)

cryp_sym = st.text_input("Token: ", "BTC")


tickerData = yf.Ticker('AAPL')
tickerDf = tickerData.history(period='1d', start='2020-5-31', end='2023-5-31')

st.line_chart(tickerDf)