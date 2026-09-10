class Produto:
    def __init__(self, categoria:str, nome:str, preco:float, quantidade_estoque:int, prazo_garantia:int, taxa_comissao):
        self.categoria = categoria
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.prazo_garantia = prazo_garantia
        self.taxa_comissao = taxa_comissao
        
    def deduzir_estoque(self, quantidade):
        self.quantidade_estoque -= quantidade

        