class GeradorComprovante:
    def gerar(venda) -> str:
        linhas = []
        linhas.append("=" * 50)
        linhas.append("      CASA & CONFORTO - COMPROVANTE DE VENDA")
        linhas.append("=" * 50)
        linhas.append(f"Venda nº: {venda.numero}")
        linhas.append(f"Data: {venda.data.strftime('%d/%m/%Y %H:%M')}")
        linhas.append(f"Cliente: {venda.cliente.nome} (CPF: {venda.cliente.cpf})")
        linhas.append(f"Vendedor: {venda.vendedor.nome}")
        linhas.append("-" * 50)
        for item in venda.get_itens():
            linhas.append(item.get_descricao())
        linhas.append("-" * 50)
        linhas.append(f"Subtotal: R$ {venda.subtotal_bruto():.2f}")
        linhas.append(f"Forma de pagamento: {venda.forma_pagamento.descricao()}")
        linhas.append(f"VALOR FINAL: R$ {venda.valor_final():.2f}")
        linhas.append("=" * 50)
        return "\n".join(linhas)
