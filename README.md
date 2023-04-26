# NBP exchange rates
This is a simple Flask application that exposes endpoints to query exchange rate data from the Narodowy Bank Polski's public APIs.

## Getting Started
To get started with the application, you can follow these steps:

1. Clone the repository:
```
git clone https://github.com/Zawalisz/nbp-exchange-rates.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python nbp_exchange_rates.py
```
The application will be available at http://localhost:5000.

## Usage
The API has the following endpoints:

### 1. Get the average exchange rate for a given date and currency code
To get the average exchange rate for a specific date and currency code, make a GET request to the following endpoint:
```
/exchanges/<currency_code>/<date>
```
***currency_code***: The 3-letter code for the currency you want to get the exchange rate for.  
***date***: The date you want to get the exchange rate for, in the format YYYY-MM-DD.  

For example, to get the average exchange rate for GBP on January 2, 2023:
```
GET /exchanges/GBP/2023-01-02
```
The response will be a JSON object with the average exchange rate for the specified currency and date.

### 2. Get the maximum and minimum exchange rate for a given currency code and number of recent rates
To get the maximum and minimum exchange rate for a specific currency code and number of recent rates, make a GET request to the following endpoint:
```
/exchanges/<currency_code>/<num_of_rates>
```
***currency_code***: The 3-letter code for the currency you want to get the exchange rate for.  
***num_of_rates***: The number of recent rates you want to get the maximum and minimum exchange rate for. The maximum value is 255.  

For example, to get the maximum and minimum exchange rate for the last 10 rates of GBP:
```
GET /exchanges/GBP/10
```
The response will be a JSON object with the maximum and minimum exchange rate for the specified currency and number of rates.

### 3. Get the major difference between buying and selling exchange rates for a given currency code and number of recent rates
To get the major difference between buying and selling exchange rates for a specific currency code and number of recent rates, make a GET request to the following endpoint:
```
/exchanges/difference/<currency_code>/<num_of_rates>
```
***currency_code***: The 3-letter code for the currency you want to get the exchange rate for.  
***num_of_rates***: The number of recent rates you want to get the major difference between buying and selling exchange rates for. The maximum value is 255.  

For example, to get the major difference between buying and selling exchange rates for the last 20 rates of USD:
```
GET /exchanges/difference/USD/20
```
The response will be a JSON object with the major difference between buying and selling exchange rates for the specified currency and number of rates.

## Running Tests
To run the tests for the application, run the following command:
```
python -m pytest
```
