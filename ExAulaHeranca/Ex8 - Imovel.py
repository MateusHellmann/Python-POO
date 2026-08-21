class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, iptu):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu

    def obter_parcela_IPTU(self):
        return self.iptu / 12

    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor
        print(f"Novo valor do aluguel: R$ {self.valor_aluguel:.2f}")


class Casa(Imovel):
    def __init__(
        self,
        inscricao_municipal,
        valor_aluguel,
        iptu,
        piscina,
        sala_de_estar,
        quartos,
        churrasqueira
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)

        self.piscina = piscina
        self.sala_de_estar = sala_de_estar
        self.quartos = quartos
        self.churrasqueira = churrasqueira


class Condominio(Imovel):
    def __init__(
        self,
        inscricao_municipal,
        valor_aluguel,
        iptu,
        area_m2,
        elevador,
        area_de_lazer
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)

        self.area_m2 = area_m2
        self.elevador = elevador
        self.area_de_lazer = area_de_lazer


class Apartamento(Imovel):
    def __init__(
        self,
        inscricao_municipal,
        valor_aluguel,
        iptu,
        quartos,
        elevador,
        area_de_lazer
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)

        self.quartos = quartos
        self.elevador = elevador
        self.area_de_lazer = area_de_lazer


class Terreno(Imovel):
    def __init__(
        self,
        inscricao_municipal,
        valor_aluguel,
        iptu,
        area_m2
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)

        self.area_m2 = area_m2


class Chacara(Imovel):
    def __init__(
        self,
        inscricao_municipal,
        valor_aluguel,
        iptu,
        area_m2,
        piscina,
        churrasqueira
    ):
        super().__init__(inscricao_municipal, valor_aluguel, iptu)

        self.area_m2 = area_m2
        self.piscina = piscina
        self.churrasqueira = churrasqueira