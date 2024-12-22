from flask import Flask, request
from flask_cors import CORS

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return 'Hello, World'

if __name__ == "__main__":
    app.run(debug=True)
