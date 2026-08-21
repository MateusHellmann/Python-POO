class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento
    
    def alterarPreco(self):
        try:
            precoNovo = float(input("Digite o novo preço do ingresso: "))
            if precoNovo:
                self.preco = precoNovo
    
        except Exception:
            print("Valor inválido")
            
    def escolherAssento(self):
        try:
            assentoNovo = float(input("Digite o novo assento da passagem: "))
            if assentoNovo:
                self.assento = assentoNovo
    
        except Exception:
            print("Valor inválido")
            
class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito
        
    def recarregarPassagem(self):
        print("Sua passagem foi recarregada")
        
class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaoDeDesembarque, checkIn):
        super().__init__(preco, assento)
        self.portaoDeDesembarque = portaoDeDesembarque
        self.checkIn = checkIn
        
    def decolar(self):
        print("O avião decolou")