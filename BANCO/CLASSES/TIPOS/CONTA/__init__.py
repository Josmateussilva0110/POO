import abc
from classes.tipos.menu import *


class Conta(abc.ABC):
    """ Classe abstrata de conta com os métodos de extrato, depositar, sacar e transferir
    e os atributos numero, titular, saldo, limite.

    Atributos:
        numero (int): Número da conta.
        titular (str): Nome do titular da conta.
        saldo (float): Saldo atual da conta.
        limite (float): Limite de crédito da conta.

    Métodos Abstratos:
        extrato(): Obtém o extrato da conta.
        depositar(valor: float): Realiza um depósito na conta.
        sacar(valor: float): Realiza um saque na conta.
        transferir(valor: float, conta2: Conta): Transfere um valor para outra conta.
    """
    def __init__(self, numero, titular, saldo=0, limite=10000):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

        @property
        def numero(self):
            return self._numero

        @property
        def titular(self):
            return self._titular

        @property
        def saldo(self):
            return self._saldo

        @property
        def limite(self):
            return self._limite

        @numero.setter
        def numero(self, valor):
            self._numero = valor

        @titular.setter
        def titular(self, pessoa):
            self._titular = pessoa

        @saldo.setter
        def saldo(self, valor):
            self._saldo = valor

        @limite.setter
        def limite(self, valor):
            self._limite = valor

    @abc.abstractmethod
    def extrato(self):
        pass

    @abc.abstractmethod
    def depositar(self, valor):
        pass

    @abc.abstractmethod
    def sacar(self, valor):
        pass

    @abc.abstractmethod
    def transferir(self, valor, conta2):
        pass


class Historico():
    """ Classe que armazena e exibe o histórico de transações da conta.

    Atributos:
        transacoes (list): Lista que armazena as transações realizadas na conta.

    Métodos:
        add_transacoes(valor: str): Adiciona uma transação à lista de transações.
        imprimir_transacoes(): Imprime as transações armazenadas no histórico.
    """
    def __init__(self):
        self.transacoes = list()

    def add_transacoes(self, valor):
        self.transacoes.append(valor)

    def imprimir_transacoes(self):
        print(f'TRANSACOES:')
        for i in self.transacoes:
            print(f'{i}')

class Conta_Corrente(Conta):
    """ Classe que representa uma conta corrente, herdando da classe Conta.

    Atributos:
        historico (Historico): Objeto que armazena o histórico de transações da conta.
        _tipo (str): Tipo da conta ('corrente').
    
    Métodos:
        depositar(valor: float): Realiza um depósito na conta corrente.
        sacar(valor: float): Realiza um saque na conta corrente.
        imprimir_saldo(): Imprime o saldo da conta corrente.
        imprimir_conta(): Imprime os dados da conta corrente.
        transferir(valor: float, conta2: Conta): Transfere um valor para outra conta.
        extrato(): Exibe o histórico de transações da conta corrente.
        decidir_operacao(conta_c: Conta_Corrente, op: int): Realiza uma operação na conta corrente.
        buscar_conta(cpf: str, dicio: dict): Busca uma conta pelo CPF no dicionário de contas.
    """
    def __init__(self, numero, titular,  historico='', saldo=0, limite=10000):
        super().__init__(numero, titular, saldo=0, limite=10000)
        self._tipo = 'corrente'
        self.historico = Historico()

    def depositar(self, valor):
        if 0 < valor <= self._limite:
            self._saldo += valor
            self.historico.add_transacoes(f'fez um deposito de {valor}')
            print('deposito feito com sucesso.')
        else:
            print('valor invalido.')

    def sacar(self, valor):
        if self._saldo > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                self.historico.add_transacoes(f'fez um saque de {valor}')
                print('valor sacado com sucesso.')
            else:
                print('saldo insuficiente.')
        else:
            print('conta esta sem saldo.')

    def imprimir_saldo(self):
        print(f'saldo da conta = {self._saldo:.2f}')

    def imprimir_conta(self):
        print('DADOS DA CONTA:')
        print(f'numero = {self._numero}')
        print(f'nome = {self._titular.nome}')
        print(f'saldo = {self._saldo:.2f}')
    
    def transferir(self, valor, conta2):
        if self._saldo >= valor:  # self.saldo se refere ao da conta1
            self._saldo -= valor  # ta tirando da conta1
            conta2._saldo += valor
            self.historico.add_transacoes(f'transferio {valor}')
            print('transferencia concluida.')
        else:
            print('saldo invalido.')
    
    def extrato(self):
        self.historico.imprimir_transacoes()
    
    def decidir_operacao(self, conta_c, op):
        if op == 0:
            valor = ler_float('digite o valor que deseja sacar: ')
            conta_c.sacar(valor)
        if op == 1:
            valor = ler_float('digite o valor que deseja depositar: ')
            conta_c.depositar(valor)
        if op == 2:
            conta_c.imprimir_saldo()
        if op == 3:
            conta_c.extrato()
        if op == 4:
            conta_c.imprimir_conta()
    
    def buscar_conta(self, cpf, dicio):
        if cpf in dicio.keys():
            return dicio[cpf]
        else:
            print('cpf nao encontrado.')
    


class Conta_Poupanca(Conta):
    """ Classe que representa uma conta poupança, herdando da classe Conta.

    Atributos:
        historico (Historico): Objeto que armazena o histórico de transações da conta.
        _tipo (str): Tipo da conta ('poupanca').
    
    Métodos:
        depositar(valor: float): Realiza um depósito na conta poupança.
        sacar(valor: float): Realiza um saque na conta poupança.
        imprimir_saldo(): Imprime o saldo da conta poupança.
        imprimir_conta(): Imprime os dados da conta poupança.
        transferir(valor: float, conta2: Conta): Transfere um valor para outra conta.
        extrato(): Exibe o histórico de transações da conta poupança.
        decidir_operacao(conta_c: Conta_Corrente, op: int): Realiza uma operação na conta poupança.
        buscar_conta(cpf: str, dicio: dict): Busca uma conta pelo CPF no dicionário de contas.
    """
    def __init__(self, numero, titular,  historico='', saldo=0, limite=10000):
        super().__init__(numero, titular, saldo=0, limite=10000)
        self._tipo = 'poupanca'
        self.historico = Historico()
    

    def depositar(self, valor):
        if 0 < valor <= self._limite:
            self._saldo += valor
            self.historico.add_transacoes(f'fez um deposito de {valor}')
            print('deposito feito com sucesso.')
        else:
            print('valor invalido.')

    def sacar(self, valor):
        if self._saldo > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                self.historico.add_transacoes(f'fez um saque de {valor}')
                print('valor sacado com sucesso.')
            else:
                print('saldo insuficiente.')
        else:
            print('conta esta sem saldo.')

    def imprimir_saldo(self):
        print(f'saldo da conta = {self._saldo:.2f}')

    def imprimir_conta(self):
        print()
        print(linha())
        print('DADOS DA CONTA:')
        print(f'numero = {self._numero}')
        print(f'titular = {self._titular.nome}')
        print(f'saldo = {self._saldo:.2f}')
        print(f'tipo de conta = {self._tipo}')
        print(linha())
    
    def extrato(self):
        self.historico.imprimir_transacoes()

    def transferir(self, valor, conta2):
        if self._saldo >= valor:  # self.saldo se refere ao da conta1
            self._saldo -= valor  # ta tirando da conta1
            conta2._saldo += valor
            self.historico.add_transacoes(f'transferio {valor}')
            print('transferencia concluida.')
        else:
            print('saldo invalido.')

    def decidir_operacao(self, conta_c, op):
        if op == 0:
            valor = ler_float('digite o valor que deseja sacar: ')
            conta_c.sacar(valor)
        if op == 1:
            valor = ler_float('digite o valor que deseja depositar: ')
            conta_c.depositar(valor)
        if op == 2:
            conta_c.imprimir_saldo()
        if op == 3:
            conta_c.extrato()
        if op == 4:
            conta_c.imprimir_conta()
    
    def buscar_conta(self, cpf, dicio):
        if cpf in dicio.keys():
            return dicio[cpf]
        else:
            print('cpf nao encontrado.')
