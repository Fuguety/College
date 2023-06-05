class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Motorista(Pessoa):
    def __init__(self, nome, telefone, numeroCNH):
        super().__init__(nome, telefone)
        self.numeroCNH = numeroCNH

class Vendedor(Pessoa):
    def __init__(self, nome, telefone, cpf, percentualComissao):
        super().__init__(nome, telefone)
        self.cpf = cpf
        self.percentualComissao = percentualComissao

motorista = Motorista("João", "123456789", "ABC123")
print(motorista.nome)  # Acesso ao atributo herdado da classe Pessoa
print(motorista.numeroCNH)  # Acesso ao atributo específico da classe Motorista

vendedor = Vendedor("Maria", "987654321", "123456789", 10)
print(vendedor.nome)  # Acesso ao atributo herdado da classe Pessoa
print(vendedor.percentualComissao)  # Acesso ao atributo específico da classe Vendedor
