from datetime import datetime

class ItemVenda:
    def __init__(self, produto, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        if quantidade > produto.get_quantidade_estoque():
            raise ValueError(f"Estoque insuficiente para {produto.nome}.")
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario_registrado = produto.get_preco()

    def subtotal(self) -> float:
        return round(self.preco_unitario_registrado * self.quantidade, 2)

    def get_descricao(self) -> str:
        return f"{self.quantidade}x {self.produto.nome} - R$ {self.subtotal():.2f}"


class Venda:
    _proximo_numero = 1

    def __init__(self, vendedor, cliente, forma_pagamento):
        self.numero = Venda._proximo_numero
        Venda._proximo_numero += 1
        self.vendedor = vendedor
        self.cliente = cliente
        self.forma_pagamento = forma_pagamento
        self.data = datetime.now()
        self._itens = []
        self._finalizada = False

    def adicionar_item(self, produto, quantidade: int):
        if self._finalizada:
            raise RuntimeError("Não é possível alterar uma venda já finalizada.")
        item = ItemVenda(produto, quantidade)
        self._itens.append(item)
        return item

    def get_itens(self) -> list:
        return list(self._itens)

    def get_finalizada(self) -> bool:
        return self._finalizada

    def subtotal_bruto(self) -> float:
        return round(sum(item.subtotal() for item in self._itens), 2)

    def valor_final(self) -> float:
        return self.forma_pagamento.calcular_valor_final(self.subtotal_bruto())

    def finalizar(self, gerenciador_estoque) -> float:
        if self._finalizada:
            raise RuntimeError("Venda já finalizada.")
        if not self._itens:
            raise RuntimeError("Não é possível finalizar uma venda sem itens.")

        gerenciador_estoque.atualizar_estoque(self)
        comissao = self.vendedor.registrar_comissao(self)
        self.cliente.registrar_venda(self)
        self._finalizada = True
        return comissao

    def get_descricao(self) -> str:
        status = "Finalizada" if self._finalizada else "Em aberto"
        return f"Venda #{self.numero} - {self.cliente.nome} - {status}"
