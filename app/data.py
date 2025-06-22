from typing import List, Dict

class Produtos:
    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Um telefone que é inteligente",
            "preco": 1500.0,
        },
        {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Um computador que é móvel",
            "preco": 3500.0,
        },
        {
            "id": 3,
            "nome": "Tablet",
            "descricao": "Um computador que é móvel",
            "preco": 2500.0,
        }
    ]

    def listar_produtos(self):
        return self.produtos
    
    def listar_produto(self, id: int):
        for produto in self.listar_produto(id):
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Mensagens": "Produto não encontrado"}
    
    def acionar_produto(self, produto):
        self.produtos.append(produto)
        return produto