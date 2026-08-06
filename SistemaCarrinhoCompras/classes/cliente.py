from .carrinho import Carrinho

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.carrinho = Carrinho()
    
    def finalizar_pedido(self):
        if self.carrinho.produtos:
            total = self.carrinho.calcular_preco()
            print(f"\nPedido finalizado, valor total: R${total:.2f}")
            self.carrinho.produtos.clear()
        else:
            print("\nNenhum produto no carrinho.")