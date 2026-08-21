class Transporte:
    def __init__(self, marca, modelo, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10
        print(f"{self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self):
        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0

        print(f"{self.modelo} reduziu para {self.velocidade} km/h.")

    def mostrar_dados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidade: {self.velocidade} km/h")



class Terrestre(Transporte):
    def __init__(self, marca, modelo, velocidade, numero_rodas):
        super().__init__(marca, modelo, velocidade)
        self.numero_rodas = numero_rodas

    def andar_na_estrada(self):
        print(f"{self.modelo} está andando na estrada.")

    def mostrar_rodas(self):
        print(f"{self.modelo} possui {self.numero_rodas} rodas.")

class Automovel(Terrestre):
    def __init__(self, marca, modelo, velocidade, numero_rodas, numero_portas):
        super().__init__(marca, modelo, velocidade, numero_rodas)
        self.numero_portas = numero_portas

    def abrir_portas(self):
        print(f"As {self.numero_portas} portas do {self.modelo} foram abertas.")

    def buzinar(self):
        print(f"{self.modelo}: BEEP BEEP!")

class Aquatico(Transporte):
    def __init__(self, marca, modelo, velocidade, capacidade):
        super().__init__(marca, modelo, velocidade)
        self.capacidade = capacidade

    def navegar(self):
        print(f"{self.modelo} está navegando.")

    def mostrar_capacidade(self):
        print(f"{self.modelo} possui capacidade para {self.capacidade} pessoas.")


class Lancha(Aquatico):
    def __init__(self, marca, modelo, velocidade, capacidade, potencia_motor):
        super().__init__(marca, modelo, velocidade, capacidade)
        self.potencia_motor = potencia_motor

    def ligar_motor(self):
        print(f"Motor da lancha {self.modelo} ligado.")

    def mostrar_potencia(self):
        print(f"A lancha {self.modelo} possui {self.potencia_motor} HP.")


class Navio(Aquatico):
    def __init__(self, marca, modelo, velocidade, capacidade, numero_de_andares):
        super().__init__(marca, modelo, velocidade, capacidade)
        self.numero_de_andares = numero_de_andares

    def atracar(self):
        print(f"O navio {self.modelo} está atracando.")

    def mostrar_andares(self):
        print(f"O navio {self.modelo} possui {self.numero_de_andares} andares.")


class Aereo(Transporte):
    def __init__(self, marca, modelo, velocidade, altitude_maxima):
        super().__init__(marca, modelo, velocidade)
        self.altitude_maxima = altitude_maxima

    def decolar(self):
        print(f"{self.modelo} está decolando.")

    def mostrar_altitude(self):
        print(f"Altitude máxima: {self.altitude_maxima} metros.")


class AviaoMonomotor(Aereo):
    def __init__(self, marca, modelo, velocidade, altitude_maxima, numero_assentos):
        super().__init__(marca, modelo, velocidade, altitude_maxima)
        self.numero_assentos = numero_assentos

    def ligar_motor(self):
        print(f"Motor do avião {self.modelo} ligado.")

    def mostrar_assentos(self):
        print(f"O avião {self.modelo} possui {self.numero_assentos} assentos.")


class AviaoComercial(Aereo):
    def __init__(self, marca, modelo, velocidade, altitude_maxima, companhia):
        super().__init__(marca, modelo, velocidade, altitude_maxima)
        self.companhia = companhia

    def iniciar_voo(self):
        print(f"O avião da {self.companhia} iniciou o voo.")

    def mostrar_companhia(self):
        print(f"Companhia aérea: {self.companhia}")

carro1 = Automovel("Toyota", "Corolla", 0, 4, 4)
carro2 = Automovel("Honda", "Civic", 0, 4, 4)
carro3 = Automovel("Volkswagen", "Golf", 0, 4, 4)

print("\n===== AUTOMÓVEIS =====")

carro1.mostrar_dados()
carro1.mostrar_rodas()
carro1.abrir_portas()
carro1.buzinar()
carro1.andar_na_estrada()
carro1.acelerar()

print()

carro2.mostrar_dados()
carro2.mostrar_rodas()
carro2.buzinar()

print()

carro3.mostrar_dados()
carro3.mostrar_rodas()
carro3.buzinar()

lancha1 = Lancha("Focker", "240", 80, 8, 250)
lancha2 = Lancha("Ventura", "V195", 70, 7, 200)
lancha3 = Lancha("NX Boats", "290", 90, 10, 300)

print("\n===== LANCHAS =====")

lancha1.mostrar_dados()
lancha1.mostrar_capacidade()
lancha1.mostrar_potencia()
lancha1.ligar_motor()
lancha1.navegar()

print()

lancha2.mostrar_dados()
lancha2.mostrar_capacidade()
lancha2.mostrar_potencia()

print()

lancha3.mostrar_dados()
lancha3.mostrar_capacidade()
lancha3.mostrar_potencia()

navio1 = Navio("MSC", "Seaview", 40, 5000, 18)
navio2 = Navio("Royal Caribbean", "Wonder", 45, 6000, 20)
navio3 = Navio("Costa", "Smeralda", 42, 5200, 19)

print("\n===== NAVIOS =====")

navio1.mostrar_dados()
navio1.mostrar_capacidade()
navio1.mostrar_andares()
navio1.atracar()
navio1.navegar()

print()

navio2.mostrar_dados()
navio2.mostrar_capacidade()
navio2.mostrar_andares()

print()

navio3.mostrar_dados()
navio3.mostrar_capacidade()
navio3.mostrar_andares()

monomotor1 = AviaoMonomotor("Cessna", "172", 226, 4300, 4)
monomotor2 = AviaoMonomotor("Piper", "PA-28", 213, 5000, 4)
monomotor3 = AviaoMonomotor("Cirrus", "SR22", 341, 5340, 5)

print("\n===== AVIÕES MONOMOTORES =====")

monomotor1.mostrar_dados()
monomotor1.mostrar_altitude()
monomotor1.mostrar_assentos()
monomotor1.ligar_motor()
monomotor1.decolar()

print()

monomotor2.mostrar_dados()
monomotor2.mostrar_altitude()
monomotor2.mostrar_assentos()

print()

monomotor3.mostrar_dados()
monomotor3.mostrar_altitude()
monomotor3.mostrar_assentos()

comercial1 = AviaoComercial("Airbus", "A320", 840, 11800, "LATAM")
comercial2 = AviaoComercial("Boeing", "737", 850, 12500, "GOL")
comercial3 = AviaoComercial("Airbus", "A350", 903, 13100, "Azul")

print("\n===== AVIÕES COMERCIAIS =====")

comercial1.mostrar_dados()
comercial1.mostrar_altitude()
comercial1.mostrar_companhia()
comercial1.iniciar_voo()
comercial1.decolar()

print()

comercial2.mostrar_dados()
comercial2.mostrar_altitude()
comercial2.mostrar_companhia()

print()

comercial3.mostrar_dados()
comercial3.mostrar_altitude()
comercial3.mostrar_companhia()