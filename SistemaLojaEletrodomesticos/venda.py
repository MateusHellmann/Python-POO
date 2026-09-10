class Venda:
    def __init__(self, cliente, vendedor):
        self.cliente = cliente
        self.vendedor = vendedor
        self.itens = []
        self.status = "Aberta"

    def adicionar_produto(self, produto, quantidade):
        # Apenas registra a intenção, não tira do estoque ainda
        if produto.quantidade_estoque >= quantidade:
            self.itens.append({"produto": produto, "quantidade": quantidade})
        else:
            raise ValueError(f"Estoque insuficiente para {produto.nome}.")

    def finalizar(self, metodo_pagamento):
        if not self.itens:
            raise ValueError("A venda não possui itens.")

        subtotal = sum(item["produto"].preco * item["quantidade"] for item in self.itens)

        valor_final = metodo_pagamento.calcular_total(subtotal)

        comissao_total = 0

        for item in self.itens:
            prod = item["produto"]
            qtd = item["quantidade"]
            
            prod.deduzir_estoque(qtd) 
            
            comissao_item = (prod.preco * qtd) * prod.taxa_comissao
            comissao_total += comissao_item

        self.vendedor.receber_comissao(comissao_total)
        self.status = "Concluida"

        return valor_final