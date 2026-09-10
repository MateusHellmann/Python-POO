from .produto import Produto

class LinhaBranca(Produto):
    def __init__(self, nome, preco, quantidade_estoque, prazo_garantia, taxa_comissao, consumo_kwh, eficiencia):
        super().__init__("Linha Branca", nome, preco, quantidade_estoque, prazo_garantia, taxa_comissao)
        self.consumo_kwh = consumo_kwh
        self.eficiencia = eficiencia
        