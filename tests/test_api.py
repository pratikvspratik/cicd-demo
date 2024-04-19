import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items_empty(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert json.loads(response.data) == []

def test_add_item(client):
    item = {'name': 'Test Item'}
    response = client.post('/items', json=item)
    assert response.status_code == 201
    assert json.loads(response.data) == item