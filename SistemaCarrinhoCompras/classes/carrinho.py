from .produto import Produto

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
        print(f"\nProduto {produto.nome} adicionado!")
        
    def remover_produto(self, produto: Produto):
        self.produtos.remove(produto)
        print(f"\nProduto {produto.nome} removido!")
        
    def listar_produtos(self):
        cont = 0
        print("\nProdutos no carrinho")
        print("| ID | Produto")
        for produto in self.produtos:
            print(f"| {cont}  | {produto.nome} - R${produto.preco:.2f}")
            cont+=1

    def calcular_preco(self) -> float:
        soma = 0
        for p in self.produtos:
            soma += p.preco
        return soma