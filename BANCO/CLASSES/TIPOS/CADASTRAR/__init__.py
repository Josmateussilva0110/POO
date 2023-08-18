from classes.tipos.menu import *
from classes.tipos.classe_conta import *


class Cadastrar_Cliente():
    """Classe para cadastrar clientes.

    Atributos:
        nome (str): Nome do cliente.
        cpf (str): CPF do cliente.

    Métodos:
        imprimir(): Imprime os dados do cliente (nome e CPF).
    """
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor

    def imprimir(self):
        print('DADOS:')
        print(f'nome - {self._nome}\ncpf - {self._cpf}')


class Salvar():
    """Classe para armazenar e manipular dados de clientes.

    Atributos:
        dados (list): Lista que armazena os objetos Cadastrar_Cliente.

    Métodos:
        armazenar(pessoa: Cadastrar_Cliente): Armazena um objeto Cadastrar_Cliente na lista.
        imprimir(tota_contas: bool = False, tota_seguro: bool = False, flag: bool = False):
        Imprime os dados cadastrados na lista e, opcionalmente, informações adicionais sobre contas e seguros.
        buscar_pessoa(cpf: str, inicio: int = 0, fim: int = None): Busca um cliente na lista pelo CPF.
        conta_sem_cadastro(): Verifica se há clientes cadastrados na lista.
    """
    def __init__(self):
        self.dados = list()

    def armazenar(self, pessoa):
        if pessoa not in self.dados:
            self.dados.append(pessoa)
            self.dados.sort(key=lambda p: p.cpf)
        else:
            print('pessoa nao cadastrada')

    def imprimir(self, tota_contas=False, tota_seguro=False, flag=False):
        if len(self.dados) == 0:
            print('nao ah pessoas cadastradas no banco')
        else:
            if flag:
                print(f'quantidade de pessoas cadastradas = {len(self.dados)}')
            cabecalho('DADOS CADASTRADOS')
            print('CPF           NOME')
            for i in self.dados:
                print(f'{i.cpf:<13}{i.nome:<20}')
            if tota_contas:
                cabecalho('TOTAL DE CONTAS')
                for i, v in tota_contas.items():
                    print(f'cpf = {i} - contas = {v}')
            if tota_seguro:
                cabecalho('TOTAL DE SEGUROS:')
                for i, v in tota_seguro.items():
                    print(f'cpf = {i} - seguros = {v}')

    def buscar_pessoa(self, cpf, inicio=0, fim=None):
        if fim is None:
            fim = len(self.dados) - 1

        if inicio <= fim:
            meio = (inicio + fim) // 2

            if self.dados[meio].cpf == cpf:
                return self.dados[meio]

            if cpf < self.dados[meio].cpf:
                return self.buscar_pessoa(cpf, inicio, meio - 1)
            else:
                return self.buscar_pessoa(cpf, meio + 1, fim)

        return None
    

    def conta_sem_cadastro(self):
        if len(self.dados) == 0:
            return True
        else:
            return False


class SeguroVida():
    """Classe para representar um seguro de vida.

    Atributos:
        valor_mensal (float): Valor mensal do seguro de vida.
        valor_total (float): Valor total do seguro de vida.
        seguros (dict): Dicionário que armazena os seguros de vida por CPF.

    Métodos:
        __str__(): Retorna uma representação em string do objeto SeguroVida.
        criar_seguro(cliente: Cadastrar_Cliente, valor_mensal: float, valor_total: float):
        Cria e armazena um novo seguro de vida no dicionário de seguros.
        imprimir_seguros(): Imprime as informações de todos os seguros de vida cadastrados.
    """
    def __init__(self, valor_mensal = 0, valor_total = 0):
        self.valor_mensal = valor_mensal
        self.valor_total = valor_total
        self.seguros = dict()

    def __str__(self):
        return f"Seguro de Vida: Valor Mensal: {self.valor_mensal}, Valor Total: {self.valor_total}"
    
    def criar_seguro(self, cliente, valor_mensal, valor_total):
        seguro = SeguroVida(valor_mensal, valor_total)
        self.seguros[cliente._cpf] = {'nome': cliente.nome, 'seguro': seguro}

    def imprimir_seguros(self):
        for cpf, info in self.seguros.items():
            nome = info['nome']
            seguro = info['seguro']
            print(f'Nome: {nome}\nCPF: {cpf}\nValor Mensal: {seguro.valor_mensal}\nValor Total: {seguro.valor_total}\n')


class Calcular_Tributacao():
    """Classe para calcular a tributação dos clientes.

    Atributos:
        total_tributacao (float): Valor total da tributação calculada.
        pessoas (Salvar): Objeto da classe Salvar contendo os dados dos clientes.

    Métodos:
        calcular(): Calcula a tributação de todos os clientes e imprime o valor total.
    """
    def __init__(self, pessoas):
        self.total_tributacao = 0
        self.pessoas = pessoas

    def calcular(self):
        for cliente in self.pessoas.dados: 
            tributacao = 10 + cliente.conta_corrente.saldo * 0.01
            for cpf, info in cliente.seguros.items(): 
                seguro = info['seguro']
                tributacao += seguro.valor_mensal * 0.02
            self.total_tributacao += tributacao
        print(f'total de tributacao dos clientes = {self.total_tributacao}')
