from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

HEADERS = {"X-API-Key": "secret123"}


def test_credit_transaction():
    response = client.post(
        "/transactions",
        json={"amount": 500, "type": "credit"},
        headers=HEADERS
    )
    assert response.status_code == 201
    assert response.json()["amount"] == 500


def test_debit_transaction():
    response = client.post(
        "/transactions",
        json={"amount": 200, "type": "debit"},
        headers=HEADERS
    )
    assert response.status_code == 201


def test_insufficient_balance():
    response = client.post(
        "/transactions",
        json={"amount": 1000, "type": "debit"},
        headers=HEADERS
    )
    assert response.status_code == 400


def test_balance():
    response = client.get("/balance", headers=HEADERS)
    assert response.status_code == 200
    assert "balance" in response.json()
