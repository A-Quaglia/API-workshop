from typing import List
from app.data import Produtos
from fastapi import FastAPI
from app.schema import ProdutosSchema

app = FastAPI()
lista_de_produtos = Produtos()

@app.get('/') # Request
def ola_mundo(): # Response
    return {"Olá": "Mundo"}

@app.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos():
    return lista_de_produtos.produtos

@app.get("/produtos/{id}", response_model=ProdutosSchema)
def buscar_produto(id: int):
    return lista_de_produtos.buscar_produto(id)
