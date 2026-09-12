from produtos import Eletroportatil
from pagamento import PagamentoAVista, PagamentoParcelado
from comprovante import GeradorComprovante
from sistema import SistemaVendas

# ------------------------------- utilidades de entrada -------------------------------

def ler_inteiro(mensagem: str) -> int:
    while True:
        valor = input(mensagem).strip()
        try:
            return int(valor)
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_float(mensagem: str) -> float:
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Digite um número válido (use ponto ou vírgula para casas decimais).")


def ler_float_opcional(mensagem: str, padrao: float) -> float:
    valor = input(mensagem).strip().replace(",", ".")
    if valor == "":
        return padrao
    try:
        return float(valor)
    except ValueError:
        print(f"Valor inválido, usando o padrão ({padrao}).")
        return padrao


def escolher_da_lista(lista, mensagem_vazio, formatar=str):
    if not lista:
        print(mensagem_vazio)
        return None
    for indice, item in enumerate(lista, start=1):
        print(f"  {indice} - {formatar(item)}")
    while True:
        escolha = ler_inteiro("Escolha o número: ")
        if 1 <= escolha <= len(lista):
            return lista[escolha - 1]
        print("Opção inválida, tente novamente.")


# ------------------------------- ações do menu -------------------------------

def cadastrar_categoria(sistema: SistemaVendas) -> None:
    print("\n--- Cadastro de categoria ---")
    nome = input("Nome da categoria: ").strip()
    percentual = ler_float("Percentual de comissão sobre a categoria (%): ")
    try:
        categoria = sistema.cadastrar_categoria(nome, percentual)
        print(f"Categoria '{categoria.get_nome()}' cadastrada com sucesso.")
    except ValueError as erro:
        print(f"Erro ao cadastrar categoria: {erro}")


def cadastrar_produto(sistema: SistemaVendas) -> None:
    print("\n--- Cadastro de produto ---")

    id_produto = input("Código/ID do produto: ").strip()
    if sistema.buscar_produto(id_produto) is not None:
        print(f"Já existe um produto cadastrado com o código '{id_produto}'.")
        return

    nome = input("Nome do produto: ").strip()
    preco = ler_float("Preço (R$): ")
    quantidade_estoque = ler_inteiro("Quantidade em estoque: ")

    print("Categorias cadastradas:")
    categoria = escolher_da_lista(
        sistema.categorias, "Nenhuma categoria cadastrada.", lambda c: c.get_nome()
    )
    if categoria is None:
        return

    prazo_garantia = ler_inteiro("Prazo de garantia (meses): ")

    try:
        if categoria == sistema.categorias[0]:  # Linha Branca
            consumo = ler_float("Consumo de energia (kWh/mês): ")
            eficiencia = input("Classificação de eficiência energética (ex.: A, B, C): ").strip().upper()
            produto = sistema.cadastrar_linha_branca(
                id_produto, nome, preco, quantidade_estoque, categoria,
                prazo_garantia, consumo, eficiencia,
            )
        elif categoria == sistema.categorias[1]:  # Eletroportáteis
            while True:
                print(f"Voltagens válidas: {', '.join(Eletroportatil.VOLTAGENS_VALIDAS)}")
                voltagem = input("Voltagem: ").strip()
                if voltagem in Eletroportatil.VOLTAGENS_VALIDAS:
                    break
                print("Voltagem inválida. Tente novamente.")
            produto = sistema.cadastrar_eletroportatil(
                id_produto, nome, preco, quantidade_estoque, categoria,
                prazo_garantia, voltagem,
            )
        else:
            produto = sistema.cadastrar_produto(
                id_produto, nome, preco, quantidade_estoque, categoria, prazo_garantia
            )
        print(f"\nProduto '{produto.nome}' cadastrado com sucesso.")
    except ValueError as erro:
        print(f"Erro ao cadastrar produto: {erro}")


def cadastrar_cliente(sistema: SistemaVendas) -> None:
    print("\n--- Cadastro de cliente ---")
    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone (opcional): ").strip() or None
    email = input("E-mail (opcional): ").strip() or None
    cliente = sistema.cadastrar_cliente(nome, cpf, telefone, email)
    print(f"\nCliente '{cliente.nome}' cadastrado com sucesso.")


def cadastrar_vendedor(sistema: SistemaVendas) -> None:
    print("\n--- Cadastro de vendedor ---")
    nome = input("Nome do vendedor: ").strip()
    matricula = input("Matrícula: ").strip()
    vendedor = sistema.cadastrar_vendedor(nome, matricula)
    print(f"\nVendedor '{vendedor.nome}' cadastrado com sucesso.")


def listar_produtos(sistema: SistemaVendas) -> None:
    print("\n--- Produtos cadastrados ---")
    if not sistema.produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in sistema.produtos:
        print(f"[{produto.id}] - Nome: {produto.descricao_detalhada()} | Estoque: {produto.get_quantidade_estoque()}")


def escolher_forma_pagamento():
    print("Forma de pagamento:")
    print("  1 - À vista")
    print("  2 - Parcelado")
    tipo = ler_inteiro("Escolha: ")
    if tipo == 1:
        percentual = ler_float_opcional("Percentual de desconto (%) [padrão 5]: ", 5.0)
        try:
            return PagamentoAVista(percentual)
        except ValueError as erro:
            print(f"Erro: {erro}")
            return None
    elif tipo == 2:
        numero_parcelas = ler_inteiro("Número de parcelas: ")
        acrescimo = ler_float_opcional("Percentual de acréscimo por parcela (%) [padrão 1.5]: ", 1.5)
        try:
            return PagamentoParcelado(numero_parcelas, acrescimo)
        except ValueError as erro:
            print(f"Erro: {erro}")
            return None
    else:
        print("Opção inválida.")
        return None


def realizar_venda(sistema: SistemaVendas) -> None:
    if not sistema.vendedores or not sistema.clientes or not sistema.produtos:
        print("\nNão é possível realizar uma venda sem vendedor, cliente ou produto cadastrados.")
        return
    print("\n--- Nova venda ---")

    print("Selecione o vendedor:")
    vendedor = escolher_da_lista(
        sistema.vendedores, "Nenhum vendedor cadastrado. Cadastre um vendedor primeiro.",
        lambda v: v.get_descricao(),
    )
    if vendedor is None:
        return

    print("Selecione o cliente:")
    cliente = escolher_da_lista(
        sistema.clientes, "Nenhum cliente cadastrado. Cadastre um cliente primeiro.",
        lambda c: c.get_descricao(),
    )
    if cliente is None:
        return

    forma_pagamento = escolher_forma_pagamento()
    if forma_pagamento is None:
        return

    venda = sistema.iniciar_venda(vendedor, cliente, forma_pagamento)

    print("\nAdicione os itens da venda:")
    while True:
        if not sistema.produtos:
            print("Não há produtos cadastrados.")
            break

        print("\nProdutos disponíveis:")
        for produto in sistema.produtos:
            print(f"  [{produto.id}] {produto.nome} - R$ {produto.get_preco():.2f} "
                  f"(estoque: {produto.get_quantidade_estoque()})")

        id_produto = input("Código do produto (Enter para encerrar os itens): ").strip()
        if id_produto == "":
            break

        produto = sistema.buscar_produto(id_produto)
        if produto is None:
            print("Produto não encontrado.")
            continue

        quantidade = ler_inteiro("Quantidade: ")
        try:
            venda.adicionar_item(produto, quantidade)
            print(f"Item adicionado: {quantidade}x {produto.nome}")
        except ValueError as erro:
            print(f"Erro ao adicionar item: {erro}")

    if not venda.get_itens():
        print("Venda cancelada: nenhum item foi adicionado.")
        sistema.cancelar_venda(venda)
        return

    try:
        comissao = sistema.finalizar_venda(venda)
    except RuntimeError as erro:
        print(f"Erro ao finalizar venda: {erro}")
        return

    print(f"\nVenda #{venda.numero} finalizada com sucesso! Comissão do vendedor: R$ {comissao:.2f}")
    print()
    print(GeradorComprovante.gerar(venda))


def ver_comprovante(sistema: SistemaVendas) -> None:
    print("\n--- Comprovante de venda ---")
    venda = escolher_da_lista(sistema.vendas, "Nenhuma venda registrada.", lambda v: v.get_descricao())
    if venda is None:
        return
    print()
    print(GeradorComprovante.gerar(venda))


def ver_historico_cliente(sistema: SistemaVendas) -> None:
    print("\n--- Histórico de vendas do cliente ---")
    cliente = escolher_da_lista(sistema.clientes, "Nenhum cliente cadastrado.", lambda c: c.get_descricao())
    if cliente is None:
        return
    historico = cliente.get_historico_vendas()
    if not historico:
        print(f"{cliente.nome} ainda não possui vendas registradas.")
        return
    print(f"\nHistórico de {cliente.nome}:")
    for venda in historico:
        print(f"  {venda.get_descricao()} - Valor final: R$ {venda.valor_final():.2f}")


# ------------------------------- menu principal -------------------------------

def exibir_menu() -> None:
    print("\n" + "=" * 50)
    print("   CASA & CONFORTO - SISTEMA DE GESTÃO DE VENDAS")
    print("=" * 50)
    print("1 - Cadastrar categoria")
    print("2 - Cadastrar produto")
    print("3 - Cadastrar cliente")
    print("4 - Cadastrar vendedor")
    print("5 - Listar produtos")
    print("6 - Realizar venda")
    print("7 - Ver comprovante de uma venda")
    print("8 - Ver histórico de vendas de um cliente")
    print("0 - Sair")


def main() -> None:
    sistema = SistemaVendas()
    acoes = {
        1: cadastrar_categoria,
        2: cadastrar_produto,
        3: cadastrar_cliente,
        4: cadastrar_vendedor,
        5: listar_produtos,
        6: realizar_venda,
        7: ver_comprovante,
        8: ver_historico_cliente,
    }

    print("Bem-vindo ao sistema de gestão de vendas da Casa & Conforto!")

    while True:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 0:
            print("\nEncerrando o sistema.")
            break

        acao = acoes.get(opcao)
        if acao is None:
            print("Opção inválida, tente novamente.")
            continue

        acao(sistema)


if __name__ == "__main__":
    main()
