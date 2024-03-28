import pytest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200

def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {'Olá': 'Mundo'}

def test_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_produtos_type():
    response = client.get("/produtos")
    assert type(response.json()) == list

def test_len_produtos_type():
    response = client.get("/produtos")
    assert len(response.json()) == 3

def test_pega_um_produto():
    response = client.get("/produtos/1")
    assert response.json() == dict(id=1,
        nome="Smartphone",
        descricao="Um telefone que é inteligente",
        preco=1500.0,
        disponivel=True)