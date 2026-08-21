class Ingresso:
    def __init__(self, preco:float, setor):
        self.preco = preco
        self.setor = setor
        
    def alterarPreco(self):
        try:
            precoNovo = float(input("Digite o novo preço do ingresso: "))
            if precoNovo:
                self.preco = precoNovo
    
        except Exception:
            print("Valor inválido")
    
    def mostrarSetor(self):
        print(f"Setor do ingresso: {self.setor}")
    
class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote:bool, openBar:bool, openFood:bool, estacionamento:bool):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.openBar = openBar
        self.openFood = openFood
        self.estacionamento = estacionamento
        
    def pegarBebida(self):
        if self.openBar:
            print("Você pôde pegar uma bebida")
        else:
            print("Você não tem acesso as bebidas")
        
    def acessarCamarote(self):
        if self.camarote:
            print("Você acessou o camarote")
        else:
            print("Você não tem acesso ao camarote")
                