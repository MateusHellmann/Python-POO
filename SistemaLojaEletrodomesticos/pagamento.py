class FormaPagamento():
    def calcular_valor_final(self, valor_bruto: float) -> float:
        raise NotImplementedError

    def descricao(self) -> str:
        raise NotImplementedError

class PagamentoAVista(FormaPagamento):
    def __init__(self, percentual_desconto: float = 5.0):
        if percentual_desconto < 0:
            raise ValueError("O percentual de desconto não pode ser negativo.")
        self.percentual_desconto = percentual_desconto

    def calcular_valor_final(self, valor_bruto: float) -> float:
        desconto = valor_bruto * (self.percentual_desconto / 100)
        return round(valor_bruto - desconto, 2)

    def descricao(self) -> str:
        return f"À vista ({self.percentual_desconto:.0f}% de desconto)"

class PagamentoParcelado(FormaPagamento):
    def __init__(self, numero_parcelas: int, percentual_acrescimo_parcela: float = 1.5):
        if numero_parcelas < 1:
            raise ValueError("O número de parcelas deve ser pelo menos 1.")
        if percentual_acrescimo_parcela < 0:
            raise ValueError("O percentual de acréscimo não pode ser negativo.")
        self.numero_parcelas = numero_parcelas
        self.percentual_acrescimo_parcela = percentual_acrescimo_parcela

    def calcular_valor_final(self, valor_bruto: float) -> float:
        acrescimo_total = self.percentual_acrescimo_parcela * (self.numero_parcelas - 1)
        valor_final = valor_bruto * (1 + acrescimo_total / 100)
        return round(valor_final, 2)

    def valor_parcela(self, valor_bruto: float) -> float:
        return round(self.calcular_valor_final(valor_bruto) / self.numero_parcelas, 2)

    def descricao(self) -> str:
        return f"Parcelado em {self.numero_parcelas}x (+{self.percentual_acrescimo_parcela}% a.m.)"
