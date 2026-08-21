class Pagamento:
    def __init__(self, valorCompra):
        self.valorCompra = valorCompra
        self.tipoPagamento = ""
        self.valorFinal = 0
        
    def processarPagamento(self):
        self.valorFinal = self.valorCompra
        
    def emitirRecibo(self):
        print(f"""
Nota Fiscal
---------------
Valor da compra: R$ {self.valorCompra:.2f}
Forma de pagamento: {self.tipoPagamento}

Total: R$ {self.valorFinal:.2f}   
---------------             
              """)
        
    def realizarPagamento(self):
        self.processarPagamento()
        self.emitirRecibo()
        
class PagamentoCredito(Pagamento):
    def __init__(self, valorCompra):
        super().__init__(valorCompra)
        self.tipoPagamento = "Cartão de crédito"
        
    def processarPagamento(self):
        self.juros = self.valorCompra * 0.1
        self.valorFinal = self.valorCompra + self.juros
        
    def selecionarParcelamento(self):
        print("\nOpções de parcelamento:")
        print(f"1. 1 x R$ {self.valorFinal:.2f}")
        print(f"2. 2 x R$ {self.valorFinal/2:.2f}")
        print(f"3. 3 x R$ {self.valorFinal/3:.2f}")
        print(f"4. 4 x R$ {self.valorFinal/4:.2f}")
        print(f"5. 5 x R$ {self.valorFinal/5:.2f}")
        print(f"6. 6 x R$ {self.valorFinal/6:.2f}")
        print(f"7. 7 x R$ {self.valorFinal/7:.2f}")
        print(f"8. 8 x R$ {self.valorFinal/8:.2f}")
        print(f"9. 9 x R$ {self.valorFinal/9:.2f}")
        print(f"10. 10 x R$ {self.valorFinal/10}")
        while True:
            try:
                qtdeParcelas = int(input("\nDigite a opção de parcelamento da compra: "))
                if qtdeParcelas > 0 and qtdeParcelas < 11:
                    self.qtdeParcelas = qtdeParcelas
                    break
                else:
                    raise Exception
                    
            except Exception:
                print("Opção inválida")
                continue
        
            
    def emitirRecibo(self):
        print(f"""
Nota Fiscal
---------------
Valor da compra: R$ {self.valorCompra:.2f}
Forma de pagamento: {self.tipoPagamento}

Juros: R$ {self.juros:.2f}

Opção de parcelamento: {self.qtdeParcelas} x R$ {self.valorFinal/self.qtdeParcelas:.2f}
                
Total: R$ {self.valorFinal:.2f}       
---------------       
            """)
        
    def realizarPagamento(self):
        self.processarPagamento()
        self.selecionarParcelamento()
        self.emitirRecibo()
    
class PagamentoDebito(Pagamento):
    def __init__(self, valorCompra):
        super().__init__(valorCompra)
        self.tipoPagamento = "Cartão de débito"
        
    def processarPagamento(self):
        return super().processarPagamento()
        
    def emitirRecibo(self):
        return super().emitirRecibo()
        
    def realizarPagamento(self):
        return super().realizarPagamento()
        
class PagamentoPix(Pagamento):
    def __init__(self, valorCompra):
        super().__init__(valorCompra)
        self.tipoPagamento = "PIX"
        
    def processarPagamento(self):
        self.desconto = self.valorCompra * 0.05
        self.valorFinal = self.valorCompra - self.desconto
            
    def emitirRecibo(self):
        print(f"""
Nota Fiscal
---------------
Valor da compra: R$ {self.valorCompra:.2f}
Forma de pagamento: {self.tipoPagamento}

Desconto: R$ {self.desconto:.2f}

Total: R$ {self.valorFinal:.2f}       
---------------       
            """)
        
    def realizarPagamento(self):
        return super().realizarPagamento()