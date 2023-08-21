from tipos.funcoes_aux import *
from tipos.class_pessoa import *

class Armazenar():
    """
    Classe que gerencia o armazenamento de produtos e pessoas.

    Atributos:
        _produtos (list): Lista de produtos.
        _gerentes (list): Lista de gerentes.
        _funcionarios (list): Lista de funcionários.

    Métodos:
        armazenar_produtos(prod): Armazena um produto na lista de produtos.
        armazenar_pessoas(pessoa): Armazena uma pessoa (gerente ou funcionário) na lista correspondente.
        imprimir_produtos(): Imprime a lista de produtos formatada.
        imprimir_um_produto(produto): Imprime os detalhes de um produto específico.
        imprimir_pessoa(tipo): Imprime a lista de pessoas (gerentes ou funcionários) formatada.
        buscar_produto(codigo, inicio=0, fim=None): Busca um produto pelo código usando busca binária.
        buscar_senha_gerente(senha): Verifica se uma senha corresponde a algum gerente.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da classe Armazenar.
        """
        self._produtos = list()
        self._gerentes = list()
        self._funcionarios = list()

    def armazenar_produtos(self, prod):
        """
        Armazena um produto na lista de produtos.

        Args:
            prod: Produto a ser armazenado.
        """
        if prod not in self._produtos:
            if prod._quant == 0:
                print('nao pode cadastrar produto com quantidade 0.')
            else:
                self._produtos.append(prod)
                self._produtos.sort(key=lambda produto: produto._codigo)
                print('produto cadastrado com sucesso.')

    def armazenar_pessoas(self, pessoa):
        """
        Armazena uma pessoa (gerente ou funcionário) na lista correspondente.

        Args:
            pessoa: Pessoa a ser armazenada.
        """
        if isinstance(pessoa, Gerente):
            self._gerentes.append(pessoa)
        elif isinstance(pessoa, Funcionario):
            self._funcionarios.append(pessoa)

    def imprimir_produtos(self):
        """
        Imprime a lista de produtos formatada.
        """
        if len(self._produtos) == 0:
            print('nao ah produtos cadastrados.')
        else:
            cabecalho('PRODUTOS:', 63)
            print('{:<8} {:<25} {:>10} {:>10}'.format('CODIGO', 'NOME', 'PREÇO', 'QUANTIDADE'))
            print(linha(63))
            for i in self._produtos:
                nome_format = i._nome[:25].ljust(25)
                preco_format = '{:>10.2f}'.format(i._preco)
                quant_format = str(i._quant).rjust(10)
                print('{:<8} {:<25} {:>10} {:>10}'.format(i._codigo, nome_format, preco_format, quant_format))
            print(linha(63))

    def imprimir_um_produto(self, produto):
        """
        Imprime os detalhes de um produto específico.

        Args:
            produto: Produto a ser impresso.
        """
        cabecalho('PRODUTO:', 63)
        print('{:<8} {:<25} {:>10} {:>10}'.format('CODIGO', 'NOME', 'PREÇO', 'QUANTIDADE'))
        print(linha(63))
        nome_format = produto._nome[:25].ljust(25)
        preco_format = '{:>10.2f}'.format(produto._preco)
        quant_format = str(produto._quant).rjust(10)
        print('{:<8} {:<25} {:>10} {:>10}'.format(produto._codigo, nome_format, preco_format, quant_format))
        print(linha(63))

    def imprimir_pessoa(self, tipo):
        """
        Imprime a lista de pessoas (gerentes ou funcionários) formatada.

        Args:
            tipo (list): Lista de pessoas a serem impressas.
        """
        if len(tipo) == 0:
            print('nao ah pessoas cadastradas.')
        else:
            cabecalho('PESSOAS:', 63)
            print('{:<8} {:<25} {:<10}'.format('CPF', 'NOME', 'CARGO'))
            print(linha(63))
            for i in tipo:
                nome_format = i._nome[:25].ljust(25)
                print('{:<8} {:<25} {:<10}'.format(i._cpf, nome_format, i.cargo))
            print(linha(63))

    def buscar_produto(self, codigo, inicio=0, fim=None):
        """
        Busca um produto pelo código usando busca binária.

        Args:
            codigo (int): Código do produto a ser buscado.
            inicio (int): Índice inicial da busca.
            fim (int): Índice final da busca.

        Returns:
            Produto: Produto encontrado ou None se não encontrado.
        """
        if fim is None:
            fim = len(self._produtos) - 1

        if inicio <= fim:
            meio = (inicio + fim) // 2

            if self._produtos[meio]._codigo == codigo:
                return self._produtos[meio]

            if codigo < self._produtos[meio]._codigo:
                return self.buscar_produto(codigo, inicio, meio - 1)
            else:
                return self.buscar_produto(codigo, meio + 1, fim)

        return None

    def buscar_senha_gerente(self, senha):
        """
        Verifica se uma senha corresponde a algum gerente.

        Args:
            senha (int): Senha a ser verificada.

        Returns:
            bool: True se a senha corresponde a um gerente, False caso contrário.
        """
        for gerente in self._gerentes:
            if gerente._senha_gerente == senha:
                return True
        return False
