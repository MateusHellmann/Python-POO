from .produto import Produto

class Eletroportatil(Produto):
    def __init__(self, nome, preco, quantidade_estoque, prazo_garantia, taxa_comissao, voltagem):
        super().__init__("Eletroportátil", nome, preco, quantidade_estoque, prazo_garantia, taxa_comissao)
        self.voltagem = voltagem