from produtos import Categoria, Produto, LinhaBranca, Eletroportatil
from pessoas import Cliente, Vendedor
from venda import Venda
from estoque import GerenciadorEstoque


class SistemaVendas:
    def __init__(self):
        self.categorias = [
            Categoria("Linha Branca", percentual_comissao=3.0),
            Categoria("Eletroportáteis", percentual_comissao=5.0),
        ]

        self.produtos = []
        self.clientes = []
        self.vendedores = []
        self.vendas = []
        self.gerenciador_estoque = GerenciadorEstoque()

    # ---- categorias ---------------------------------------------------
    def cadastrar_categoria(self, nome: str, percentual_comissao: float) -> Categoria:
        categoria = Categoria(nome, percentual_comissao)
        self.categorias.append(categoria)
        return categoria

    # ---- produtos -------------------------------------------------------
    def cadastrar_produto(self, id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses) -> Produto:
        produto = Produto(id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses)
        self.produtos.append(produto)
        return produto
    
    def cadastrar_linha_branca(self, id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses, consumo_energia_kwh_mes, classificacao_eficiencia) -> LinhaBranca:
        produto = LinhaBranca(id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses, consumo_energia_kwh_mes, classificacao_eficiencia)
        self.produtos.append(produto)
        return produto

    def cadastrar_eletroportatil(self, id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses, voltagem) -> Eletroportatil:
        produto = Eletroportatil(id, nome, preco, quantidade_estoque, categoria, prazo_garantia_meses, voltagem)
        self.produtos.append(produto)
        return produto

    def buscar_produto(self, id_produto: str):
        for produto in self.produtos:
            if produto.id == id_produto:
                return produto
        return None

    # ---- pessoas --------------------------------------------------------
    def cadastrar_cliente(self, nome, cpf, telefone=None, email=None) -> Cliente:
        cliente = Cliente(nome, cpf, telefone, email)
        self.clientes.append(cliente)
        return cliente

    def cadastrar_vendedor(self, nome, matricula) -> Vendedor:
        vendedor = Vendedor(nome, matricula)
        self.vendedores.append(vendedor)
        return vendedor

    # ---- vendas -----------------------------------------------------------
    def iniciar_venda(self, vendedor, cliente, forma_pagamento) -> Venda:
        venda = Venda(vendedor, cliente, forma_pagamento)
        self.vendas.append(venda)
        return venda

    def cancelar_venda(self, venda: Venda) -> None:
        if venda in self.vendas:
            self.vendas.remove(venda)

    def finalizar_venda(self, venda: Venda) -> float:
        return venda.finalizar(self.gerenciador_estoque)
