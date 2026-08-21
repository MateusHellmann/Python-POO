class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        
    def play(self):
        print("O filme foi retomado.")
        
class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
        
    def explodir(self):
        print("💥💥💥💥💥💥")
        
class Drama(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
        
    def chorar(self):
        print("😭😭😭😭😭")
        
class Suspense(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)
        
    def chocar(self):
        print("uou 😯😯😯😯")
        
filmeAcao = Acao("Velozes e furiosos", 120)
filmeDrama = Drama("A vida é triste", 60)
filmeSuspense = Suspense("O iluminado", 90)

filmeAcao.play()
filmeAcao.explodir()
filmeDrama.play()
filmeDrama.chorar()
filmeSuspense.play()
filmeSuspense.chocar()