from datetime import datetime
from math import radians
import pytz
from random import randint

class ContaCorrente:
    """ 
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): nome do cliente
        cpf (str): CPF do cliente. Deve ser inserido com pontos e traços.
        agencia (int): agencia responsável pela conta do cliente
        conta (int): número da conta
        _saldo (float): _saldo da conta
        limite (float): limite de cheque especial
        transações: transações ocorridas

    Métodos:
    """
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    
    def __init__(self, nome, cpf, agencia, conta):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self._saldo = 0
        self.limite = 0
        self.transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        """
            Exibe o saldo atual da conta do cliente
            Não há parâmetros necessários
        
        """
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        #metodos estáticos

    def _limite_conta(self):
        self.limite = 1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self.limite:
            print('Você não tem saldo suficiente para fazer essa transação.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite total com Cheque Especial é de R${:,.2f}'.format(self._limite_conta() + self._saldo))
        
    def consultar_historico(self):
        print('Histórico de transações:')
        print('Valor / Saldo / Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self.transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino.transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class ClaraCard:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(ClaraCard._data_hora().month, ClaraCard._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), (randint(0,9)), (randint(0, 9)))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self.numero)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Senha inválida')
            