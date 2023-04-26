from nbp_exchange_rates import app

def test_get_exchange_rate():
    with app.test_client() as client:
        response = client.get('/exchanges/EUR/2023-04-24')
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        #assert response.json() == {'mid': 4.6129}

def test_get_max_min_exchange_rate():
    with app.test_client() as client:
        response = client.get('/exchanges/USD/5')
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        assert response.json == {'max': 4.2024, 'min': 4.1557}

def test_get_exchange_rate_difference():
    with app.test_client() as client:
        response = client.get('/exchanges/difference/USD/5')
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        assert response.json == {'max_difference': 0.08420000000000005}

def test_invalid_currency_code():
    with app.test_client() as client:
        response = client.get('/exchanges/XXX/2022-01-01')
        assert response.status_code == 404
        assert response.content_type == 'application/json'
        assert response.json == {'error': 'Exchange rate not found.'}

def test_invalid_date():
    with app.test_client() as client:
        response = client.get('/exchanges/USD/2023-01-01')
        assert response.status_code == 404
        assert response.content_type == 'application/json'
        assert response.json == {'error': 'Exchange rate not found.'}

def test_invalid_num_of_rates():
    with app.test_client() as client:
        response = client.get('/exchanges/USD/0')
        assert response.status_code == 404
        assert response.content_type == 'application/json'
        assert response.json == {'error': 'Exchange rates not found.'}