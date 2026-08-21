class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
    def negociar(self):
        print(f"{self.nome} começou a negociar")
        

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        
    def apresentarDocumento(self):
            return f"{self.nome} - CPF: {self.cpf}"
    
class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        
    def apresentarDocumento(self):
        return f"{self.nome} - CNPJ: {self.cnpj}"