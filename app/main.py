from fastapi import FastAPI
from .data import Produtos
from .schema import ProductSchema

app = FastAPI()
lista_de_produtos = Produtos()

@app.get("/")
def ola_mundo():
    return {"Olá": "Mundo"}

@app.get("/produtos", response_model = list[ProductSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()

@app.get("/produtos/{id}", response_model = ProductSchema)
def listar_produto(id: int):
    return lista_de_produtos.listar_produto(id)

@app.post("/produtos/", response_model = ProductSchema)
def adicionar_produto(produto: ProductSchema):
    return lista_de_produtos.acionar_produto(produto.model_dump())