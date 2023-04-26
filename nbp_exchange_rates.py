import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint for getting the average exchange rate for a given date and currency code
@app.route('/exchanges/<currency_code>/<date>', methods=['GET'])
def get_exchange_rate(currency_code, date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{date}/'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        return jsonify(data['rates'][0]['mid'])
    else:
        return jsonify({'error': 'Exchange rate not found.'}), 404

# Endpoint for getting the maximum and minimum exchange rate for a given currency code and number of recent rates
@app.route('/exchanges/<currency_code>/<int:num_of_rates>', methods=['GET'])
def get_max_min_exchange_rate(currency_code, num_of_rates):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/last/{num_of_rates}/'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        rates = [rate['mid'] for rate in data['rates']]
        max_rate = max(rates)
        min_rate = min(rates)
        return jsonify({'max': max_rate, 'min': min_rate})
    else:
        return jsonify({'error': 'Exchange rates not found.'}), 404

# Endpoint for getting the main difference between buying and selling exchange rates for a given currency code and number of recent rates
@app.route('/exchanges/difference/<currency_code>/<int:num_of_rates>', methods=['GET'])
def get_exchange_rate_difference(currency_code, num_of_rates):
    url = f'http://api.nbp.pl/api/exchangerates/rates/c/{currency_code}/last/{num_of_rates}/'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        rates = [{'bid': rate['bid'], 'ask': rate['ask']} for rate in data['rates']]
        max_difference = max([rate['ask'] - rate['bid'] for rate in rates])
        return jsonify({'max_difference': max_difference})
    else:
        return jsonify({'error': 'Exchange rates not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)