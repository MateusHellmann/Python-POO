class PagamentoAVista:
    def calcular_total(self, subtotal):
        desconto = subtotal * 0.10 # 10% de desconto
        return subtotal - desconto

class PagamentoCartaoParcelado:
    def __init__(self, parcelas):
        self.parcelas = parcelas

    def calcular_total(self, subtotal):
        acrescimo = subtotal * (0.02 * self.parcelas) # Exemplo: 2% de juros por parcela
        return subtotal + acrescimo