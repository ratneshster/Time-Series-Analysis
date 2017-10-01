"""
    author: rkopeinig
    script: Flask Webservice to retrieve Cryptocurrency Time-Series
    description: Create REST webservice for time series analysis data using Flask
    date: 09/30/2017
    version: 0.1
"""
# Import dependencies
from flask import Flask, jsonify, render_template
from utils import get_data, mean_calculation

# GLOBAL VARIABLES
ETH='GDAX/ETH_EUR'
BTC='GDAX/EUR'
LTC='GDAX/LTC_EUR'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return 'Nothing here yet'

@app.route('/eth', methods=['GET'])
def ethereum_to_euro():
    #_eth = get_data(ETH)
    #eth = mean_calculation(_eth)
    pass

@app.route('/btc', methods=['GET'])
def bitcoin_to_euro():
    #_btc = get_data(BTC)
    #btc = mean_calculation(_btc)
    pass

@app.route('/ltc', methods=['GET'])
def litecoin_to_euro():
    #_ltc = get_data(LTC)
    #ltc = mean_calculation(_ltc)
    pass

if __name__ == '__main__':
    app.run()
