class Brinquedo:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com {self.nome}")


class BuzzLightyear(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, velocidade_voo):
        super().__init__(nome, cor, tamanho, preco)
        self.velocidade_voo = velocidade_voo

    def brincar(self):
        print(f"{self.nome} está voando pelo espaço")


class Woody(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tipo_laco):
        super().__init__(nome, cor, tamanho, preco)
        self.tipo_laco = tipo_laco

    def brincar(self):
        print(f"{self.nome} está jogando seu laço")


class Boneca(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, roupa):
        super().__init__(nome, cor, tamanho, preco)
        self.roupa = roupa

    def brincar(self):
        print(f"Estou brincando de vestir a boneca {self.nome}")


class Carrinho(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, velocidade):
        super().__init__(nome, cor, tamanho, preco)
        self.velocidade = velocidade

    def brincar(self):
        print(f"{self.nome} está correndo a {self.velocidade} km/h")


class Bola(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, esporte):
        super().__init__(nome, cor, tamanho, preco)
        self.esporte = esporte

    def brincar(self):
        print(f"Estou jogando {self.esporte} com a bola {self.nome}")


class Robo(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, tipo_movimento):
        super().__init__(nome, cor, tamanho, preco)
        self.tipo_movimento = tipo_movimento

    def brincar(self):
        print(f"O robô {self.nome} está se movimentando")


class Pipa(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, material):
        super().__init__(nome, cor, tamanho, preco)
        self.material = material

    def brincar(self):
        print(f"A pipa {self.nome} está voando no céu")


class Pelucia(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, animal):
        super().__init__(nome, cor, tamanho, preco)
        self.animal = animal

    def brincar(self):
        print(f"Estou abraçando o bichinho de pelúcia {self.nome}")


class QuebraCabeca(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, quantidade_pecas):
        super().__init__(nome, cor, tamanho, preco)
        self.quantidade_pecas = quantidade_pecas

    def brincar(self):
        print(f"Estou montando o quebra-cabeça {self.nome}")


class Lego(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco, quantidade_pecas):
        super().__init__(nome, cor, tamanho, preco)
        self.quantidade_pecas = quantidade_pecas

    def brincar(self):
        print(f"Estou construindo com o LEGO {self.nome}")