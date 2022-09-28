from random import randint
from wsgiref.validate import validator


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do valor recomendado. Caixa atual: {}'.format(self.caixa))
        else:
            print('O valor do caixa está dentro dos limites recomendados. Caixa atual: {}'.format(self.caixa))

    def emprestar(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))
        #self.caixa += patrimonio

#Agencia virtual
class AgenciaVirtual(Agencia):

    def __init__(self, telefone, cnpj, site):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.conta_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor

#Agencia comum
class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


#Agencia premium
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj, numero):
        super().__init__(telefone, cnpj, numero)
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('Esse cliente não pode ser criado com esse tipo de conta.')


if __name__ == '__main__':
    
    agencia_pp = AgenciaPremium(852, 1112222, 3100)
    agencia_pp.adicionar_cliente('Clara', 111222, 5000000)

    print(agencia_pp.clientes)