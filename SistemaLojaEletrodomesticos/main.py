from produtos import Categoria, LinhaBranca, Eletroportatil
from pessoas import Cliente, Vendedor
from pagamento import PagamentoAVista, PagamentoParcelado
from venda import Venda
from estoque import GerenciadorEstoque
from comprovante import GeradorComprovante

# ---- Categorias --------------------------------------------------------
cat_linha_branca = Categoria("Linha Branca", percentual_comissao=3.0)
cat_eletroportateis = Categoria("Eletroportáteis", percentual_comissao=5.0)

# ---- Produtos ------------------------------------------------------------
geladeira = LinhaBranca(
    id="LB001",
    nome="Geladeira Frost Free 400L",
    preco=3299.90,
    quantidade_estoque=8,
    categoria=cat_linha_branca,
    prazo_garantia_meses=12,
    consumo_energia_kwh_mes=45.0,
    classificacao_eficiencia="A",
)
liquidificador = Eletroportatil(
    id="EP001",
    nome="Liquidificador Turbo",
    preco=189.90,
    quantidade_estoque=20,
    categoria=cat_eletroportateis,
    prazo_garantia_meses=6,
    voltagem="Bivolt",
)

print("Catálogo cadastrado:")
print(f"  - {geladeira.descricao_detalhada()}")
print(f"  - {liquidificador.descricao_detalhada()}")
print()

# ---- Pessoas ---------------------------------------------------------
cliente = Cliente(nome="Ana Souza", cpf="123.456.789-00", telefone="(67) 99999-0000")
vendedor = Vendedor(nome="Carlos Lima", matricula="V-045")

gerenciador_estoque = GerenciadorEstoque()

# ---- Venda 1: parcelada -------------------------------------------------
forma_pagamento_1 = PagamentoParcelado(numero_parcelas=6, percentual_acrescimo_parcela=1.8)
venda1 = Venda(vendedor=vendedor, cliente=cliente, forma_pagamento=forma_pagamento_1)
venda1.adicionar_item(geladeira, 1)
venda1.adicionar_item(liquidificador, 2)

print(f"Estoque antes da venda 1 -> Geladeira: {geladeira.get_quantidade_estoque()}, "
        f"Liquidificador: {liquidificador.get_quantidade_estoque()}")

comissao1 = venda1.finalizar(gerenciador_estoque)

print(f"Estoque depois da venda 1 -> Geladeira: {geladeira.get_quantidade_estoque()}, "
        f"Liquidificador: {liquidificador.get_quantidade_estoque()}")
print(f"Comissão do vendedor nesta venda: R$ {comissao1:.2f}")
print()
print(GeradorComprovante.gerar(venda1))
print()

# ---- Venda 2: à vista (demonstra polimorfismo na forma de pagamento) ----
forma_pagamento_2 = PagamentoAVista(percentual_desconto=8)
venda2 = Venda(vendedor=vendedor, cliente=cliente, forma_pagamento=forma_pagamento_2)
venda2.adicionar_item(liquidificador, 1)
comissao2 = venda2.finalizar(gerenciador_estoque)

print(GeradorComprovante.gerar(venda2))
print()
print(f"Comissão do vendedor na venda 2: R$ {comissao2:.2f}")
print(f"Comissão acumulada total do vendedor: R$ {vendedor.get_comissao_acumulada():.2f}")

# ---- Histórico do cliente ----------------------------------------------
print()
print("Histórico de vendas do cliente:")
for v in cliente.get_historico_vendas():
    print(f"  {v.get_descricao()} - Valor final: R$ {v.valor_final():.2f}")

# ---- Tentativa de venda sem estoque suficiente (tratamento de erro) ----
print()
try:
    venda3 = Venda(vendedor=vendedor, cliente=cliente, forma_pagamento=PagamentoAVista())
    venda3.adicionar_item(liquidificador, 100)
except ValueError as erro:
    print(f"  Erro tratado com sucesso: {erro}")
