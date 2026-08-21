class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        
class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas:list):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = 0
        
    def calcularMedia(self):
        self.media = sum(self.notas)/len(self.notas)
    
    def estudar(self):
        print(f"Aluno {self.nome} começou a estudar.")
        
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, cargaHoraria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.cargaHoraria = cargaHoraria
        self.salario = salario
        
    def lecionar(self):
        print(f"Professor {self.nome} começou a lecionar aulas de {self.disciplina}")
        
        