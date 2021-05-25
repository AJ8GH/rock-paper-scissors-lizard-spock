# import unittest
# from flask import Flask
# from werkzeug.wrappers import response
# import app

# app.testing = True


import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_route_exists(client):
    response = client.get('/')
    assert response.status_code == 200
