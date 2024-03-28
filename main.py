from typing import Dict, List
from fastapi import FastAPI

app = FastAPI()

produtos: List[Dict[str, any]] = [
    dict(id=1,
        nome="Smartphone",
        descricao="Um telefone que é inteligente",
        preco=1500.0,
        disponivel=True),

        dict(id=2,
        nome="Notebook",
        descricao="Um computador que é móvel",
        preco=4500.0,
        disponivel=True),

        dict(id=3,
        nome="Tablet",
        descricao="Um Tablet",
        preco=3500.0,
        disponivel=True)
]


@app.get('/') # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{id}")
def buscar_produto(id: int):
    for produto in produtos:
        if produto['id'] == id:
            return produto
    return {"Status": 4040, "Mensagem": "Produto não encontrado"}
