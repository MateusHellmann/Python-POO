class GerenciadorEstoque:
    def atualizar_estoque(self, venda) -> None:
        for item in venda.get_itens():
            item.produto.dar_baixa_estoque(item.quantidade)

    def repor(self, produto, quantidade: int) -> None:
        produto.repor_estoque(quantidade)
