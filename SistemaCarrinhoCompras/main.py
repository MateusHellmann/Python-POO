from classes.cliente import Cliente
from classes.produto import Produto

clientes = []
produtos = []
    
def cadastrarProduto():
    while True:
        try:
            nomeProduto = input("Digite o nome do produto (0 para cancelar): ")
            
            if nomeProduto == "0":
                break
            
            precoProduto = float(input("Digite o preço do produto: "))
            
            produto = Produto(nomeProduto, precoProduto)
            
            produtos.append(produto)
            
            print(f"\nProduto {produto.nome} cadastrado.\n")

            continuar = input("Deseja cadastrar outro produto? (S/N) ")
            
            if continuar.lower() == "s":
                continue
            else:
                break
            
        except Exception:
            print("\nValor inválido.")
            
def cadastrarCliente():
    while True:
        try:
            nome = input("Digite o nome do cliente (0 para cancelar): ")
            
            if nome == "0":
                break
            
            email = input("Digite o email do cliente: ")
            
            cliente = Cliente(nome, email)
            
            clientes.append(cliente)
            
            print(f"\nCliente {cliente.nome} cadastrado.\n")

            continuar = input("Deseja cadastrar outro cliente? (S/N) ")
            
            if continuar.lower() == "s":
                continue
            else:
                break
            
        except Exception:
            print("\nValor inválido.")
            
def selecionarCliente():
    if clientes:
        while True:
            contCliente = 0
            print("\nClientes cadastrados:")
            print("| ID | Cliente")
            for cliente in clientes:
                print(f"| {contCliente}  | {cliente.nome}")
                contCliente+=1
                
            try:
                buscaCliente = int(input("\nDigite o ID do cliente afetado: "))
                if clientes[buscaCliente]:
                    return clientes[buscaCliente]
                else:
                    raise Exception
            except Exception:
                print("\nValor inválido")
    else:
        print("\nNenhum cliente cadastrado.")
        return None
            
def selecionarProduto(metodo, cliente = None):
    if metodo == "lista":
        if produtos:
            while True:
                contProduto = 0
                print("\nProdutos cadastrados:")
                print("| ID | Produto")
                for produto in produtos:
                    print(f"| {contProduto}  | {produto.nome} - R${produto.preco:.2f}")
                    contProduto+=1
                    
                try:
                    buscaProduto = int(input("\nDigite o ID do produto que deseja selecionar: "))
                    if produtos[buscaProduto]:
                        return produtos[buscaProduto]
                    else:
                        raise Exception
                except Exception:
                    print("\nValor inválido")
        else:
            print("\nNenhum produto cadastrado.")
            return None
    elif metodo == "carrinho":
        if cliente.carrinho.produtos:
            while True:
                cliente.carrinho.listar_produtos()
                    
                try:
                    buscaProduto = int(input("\nDigite o ID do produto que deseja selecionar: "))
                    if cliente.carrinho.produtos[buscaProduto]:
                        return cliente.carrinho.produtos[buscaProduto]
                    else:
                        raise Exception
                except Exception:
                    print("\nValor inválido")
        else:
            print("\nNenhum produto no carrinho.")
            return None
            
def adicionarProdutoCarrinho():
    cliente = selecionarCliente()
    if cliente:
        produto = selecionarProduto("lista")
        
        if produto:
            cliente.carrinho.adicionar_produto(produto)
    
    
def removerProdutoCarrinho():
    cliente = selecionarCliente()
    if cliente:
        produto = selecionarProduto("carrinho", cliente)
        
        if produto:
            cliente.carrinho.remover_produto(produto)
    
def finalizarCompra():
    cliente = selecionarCliente()
    
    if cliente:
        cliente.finalizar_pedido()
    

while True:
    print("\nSistema de Carrinho")
    print("1 - Cadastrar Produto")
    print("2 - Cadastrar Cliente")
    print("3 - Adicionar produto ao carrinho")
    print("4 - Remover produto do carrinho")
    print("5 - Finalizar compra")
    print("0 - Sair")
    
    op = int(input("\nDigite a opcao desejada: "))
    
    match op:
        case 0:
            print("\nSaindo do sistema...\n")
            break
        
        case 1:
            cadastrarProduto()
            
        case 2:
            cadastrarCliente()
            
        case 3:
            adicionarProdutoCarrinho()
        
        case 4:
            removerProdutoCarrinho()
        
        case 5:
            finalizarCompra()
        
        case _:
            print("Opção inválida\n")
                