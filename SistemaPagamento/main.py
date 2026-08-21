from classes import *

def escolherFormaPagamento(valorCompra):
    print("\nFormas de pagamento:")
    print("1. Cartão de crédito")
    print("2. Cartão de débito")
    print("3. PIX")
    while True:
        try:
            op = int(input("\nDigite a forma de pagamento desejada: "))
            match op:
                case 1:
                    return PagamentoCredito(valorCompra)
                case 2:
                    return PagamentoDebito(valorCompra)
                case 3:
                    return PagamentoPix(valorCompra)
                case _:
                    raise Exception
        except Exception:
            print("\nOpção inválida")
            continue

while True:
    try:
        valorCompra = float(input("\nDigite o valor da compra realizada: R$ "))
        
        pagamento = escolherFormaPagamento(valorCompra)
        
        pagamento.realizarPagamento()
        break
    except Exception:
        print("\nValor inválido")
    
    