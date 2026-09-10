# main.py

# Importando as classes das suas respectivas pastas
from pessoas.cliente import Cliente
from pessoas.vendedor import Vendedor
from produtos.linhaBranca import LinhaBranca
from produtos.eletroportatil import Eletroportatil
from venda import Venda
from pagamento import PagamentoAVista, PagamentoCartaoParcelado

def main():
    print("=== INICIANDO SISTEMA DA LOJA ===\n")

    # 1. Cadastrando as Pessoas
    vendedor_joao = Vendedor(id_vendedor=1, nome="João Silva")
    cliente_mateus = Cliente(nome="Mateus") # Considerando que sua classe Cliente pede um nome

    # 2. Cadastrando os Produtos (Estoque Inicial)
    # Criando um produto da Linha Branca
    geladeira = LinhaBranca(
        nome="Geladeira Brastemp Frost Free",
        preco=3500.00,
        quantidade_estoque=10,
        prazo_garantia=12,         # 12 meses
        taxa_comissao=0.05,  # 5% de comissão
        consumo_kwh=45.5,
        eficiencia="A"
    )

    # Criando um Eletroportátil
    liquidificador = Eletroportatil(
        nome="Liquidificador Arno",
        preco=150.00,
        quantidade_estoque=20,
        prazo_garantia=6,          # 6 meses
        taxa_comissao=0.03,  # 3% de comissão
        voltagem="220V"
    )

    # 3. Iniciando o Atendimento (Venda)
    print(f"Atendimento iniciado: Vendedor {vendedor_joao.nome} atendendo Cliente {cliente_mateus.nome}")
    nova_venda = Venda(cliente=cliente_mateus, vendedor=vendedor_joao)

    # O cliente pede 1 geladeira e 2 liquidificadores
    try:
        nova_venda.adicionar_produto(geladeira, quantidade=1)
        nova_venda.adicionar_produto(liquidificador, quantidade=2)
        print("Produtos adicionados à venda com sucesso.\n")
    except ValueError as erro:
        print(f"Erro ao adicionar produto: {erro}")

    # 4. Escolhendo a forma de pagamento
    # Simulando um pagamento parcelado em 3x (que possui acréscimo de acordo com a nossa regra)
    forma_de_pagamento = PagamentoCartaoParcelado(parcelas=3)

    # 5. Finalizando a Venda
    print("=== FINALIZANDO A VENDA ===")
    try:
        valor_final = nova_venda.finalizar(metodo_pagamento=forma_de_pagamento)
        print(f"Venda concluída com sucesso!")
        print(f"Valor Final (com juros do parcelamento): R$ {valor_final:.2f}\n")
    except ValueError as erro:
        print(f"Erro ao finalizar: {erro}")

    # 6. Conferindo os Resultados (Estoque e Comissões)
    print("=== RESUMO PÓS-VENDA ===")
    print("-> Status do Estoque:")
    print(f"Estoque da {geladeira.nome}: {geladeira.quantidade_estoque} unidades") # Esperado: 9
    print(f"Estoque do {liquidificador.nome}: {liquidificador.quantidade_estoque} unidades\n") # Esperado: 18

    print("-> Resumo do Vendedor:")
    vendedor_joao.exibir_resumo() 
    # Comissão esperada: 5% de 3500 (175) + 3% de 300 (9) = R$ 184.00

if __name__ == "__main__":
    main()