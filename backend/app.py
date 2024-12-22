from flask import Flask, request
from flask_cors import CORS
from routes import prices, preferences

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

app.register_blueprint(prices.bp, url_prefix='/api/prices')
app.register_blueprint(preferences.bp, url_prefix='/api/preferences')

@app.route('/')
def home():
    return 'Hello, World'

if __name__ == "__main__":
    app.run(debug=True)
