class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05

        self.valor_total = self.valor + icms + frete

        return self.valor_total


class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_preco_com_desconto(self):
        self.calcular_valor_total()

        valor_desconto = self.valor_total * (self.desconto / 100)
        preco_final = self.valor_total - valor_desconto

        return preco_final


class Parcelada(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas):
        super().__init__(numero, produto, valor)
        self.numero_parcelas = numero_parcelas

    def calcular_valor_parcela(self):
        self.calcular_valor_total()

        valor_parcela = self.valor_total / self.numero_parcelas

        return valor_parcela