class Cliente:
    def __init__(self, nome: str, cpf: str, telefone: str = None, email: str = None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self._historico_vendas = []

    def registrar_venda(self, venda) -> None:
        self._historico_vendas.append(venda)

    def get_historico_vendas(self) -> list:
        return list(self._historico_vendas)

    def get_descricao(self) -> str:
        return f"{self.nome} (CPF: {self.cpf})"


class Vendedor:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self._comissao_acumulada = 0.0

    def get_comissao_acumulada(self) -> float:
        return self._comissao_acumulada

    def calcular_comissao_venda(self, venda) -> float:
        total_comissao = 0.0
        for item in venda.get_itens():
            percentual = item.produto.categoria.get_percentual_comissao()
            total_comissao += item.subtotal() * (percentual / 100)
        return round(total_comissao, 2)

    def registrar_comissao(self, venda) -> float:
        comissao = self.calcular_comissao_venda(venda)
        self._comissao_acumulada += comissao
        return comissao

    def get_descricao(self) -> str:
        return f"{self.nome} (Mat: {self.matricula})"
