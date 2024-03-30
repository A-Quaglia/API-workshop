
from typing import Dict, List


class Produtos:
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

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self, id: int):
        for produto in self.produtos:
            if produto['id'] == id:
                return produto
        return {"Status": 4040, "Mensagem": "Produto não encontrado"}
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto