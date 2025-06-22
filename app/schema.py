from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProductSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat