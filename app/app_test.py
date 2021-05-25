import pytest

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.secret_key = 'secret'
    with app.test_client() as client:
        yield client

def test_index_route_exists(client):
    response = client.get('/')
    assert response.status_code == 200

def test_play_route(client):
    response = client.get('/play')
    assert response.status_code == 200
