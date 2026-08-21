class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self, presente):
        self.pontos.append(presente)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Salário: R$ {self.salario:.2f}")
        print(f"Pontos: {self.pontos}")


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def bater_meta(self):
        print(f"{self.nome} bateu a meta!")

    def exibir_comissao(self):
        print(f"Comissão: R$ {self.comissao:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def acessar_sistema(self, senha):
        if senha == self.senha:
            print("Acesso autorizado")
        else:
            print("Senha incorreta")