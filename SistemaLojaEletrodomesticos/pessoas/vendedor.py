class Vendedor:
    def __init__(self, id_vendedor: int, nome: str):
        self.id_vendedor = id_vendedor
        self.nome = nome
        self.saldo_comissao = 0.0  # Começa zerado
        self.historico_vendas = [] # Opcional: guarda as vendas feitas por ele

    def receber_comissao(self, valor: float):
        """Atualiza o saldo do vendedor com a comissão recebida."""
        if valor > 0:
            self.saldo_comissao += valor

    def registrar_venda(self, venda):
        """Salva a venda no histórico deste vendedor."""
        self.historico_vendas.append(venda)

    def exibir_resumo(self):
        print(f"Vendedor: {self.nome} | Comissões Acumuladas: R$ {self.saldo_comissao:.2f}")
        print(f"Total de vendas realizadas: {len(self.historico_vendas)}")