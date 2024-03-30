from pydantic import BaseModel, PositiveInt, PositiveFloat
from typing import Optional


class ProdutosSchema(BaseModel):
    id: PositiveInt
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat
    disponivel: bool

