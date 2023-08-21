import abc
from random import randint

class Pessoa(abc.ABC):
    """
    Classe abstrata que define uma pessoa genérica com nome e CPF.

    Atributos:
        _nome (str): Nome da pessoa.
        _cpf (str): CPF da pessoa.

    Métodos:
        nome: Propriedade para obter o nome da pessoa.
        cpf: Propriedade para obter o CPF da pessoa.
        nome.setter: Setter para modificar o nome da pessoa.
        cpf.setter: Setter para modificar o CPF da pessoa.
        ver_pessoa(): Método abstrato para visualizar informações da pessoa.
    """
    
    def __init__(self, nome, cpf):
        """
        Inicializa uma nova instância da classe Pessoa.

        Args:
            nome (str): Nome da pessoa.
            cpf (str): CPF da pessoa.
        """
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        """
        Propriedade para obter o nome da pessoa.
        """
        return self._nome

    @property
    def cpf(self):
        """
        Propriedade para obter o CPF da pessoa.
        """
        return self._cpf

    @nome.setter
    def nome(self, nome):
        """
        Setter para modificar o nome da pessoa.

        Args:
            nome (str): Novo nome da pessoa.
        """
        self._nome = nome

    @cpf.setter
    def cpf(self, valor):
        """
        Setter para modificar o CPF da pessoa.

        Args:
            valor (str): Novo CPF da pessoa.
        """
        self._cpf = valor
    
    @abc.abstractmethod
    def ver_pessoa(self):
        """
        Método abstrato para visualizar informações da pessoa.
        """
        pass


class Autenticacao(abc.ABC):
    """
    Classe abstrata que define um método de autenticação básico.

    Métodos Abstratos:
        autenticacao(senha): Método abstrato para autenticar com uma senha.
    """
    @abc.abstractmethod
    def autenticacao(self, senha):
        """
        Método abstrato para autenticar com uma senha.

        Args:
            senha (str): Senha a ser verificada.
        """
        pass


class Sistema_interno():
    """
    Classe que representa um sistema interno de autenticação.

    Métodos:
        login(obj, senha): Realiza o processo de login.
    """
    def login(self, obj, senha):
        """
        Realiza o processo de login.

        Args:
            obj: Objeto a ser autenticado.
            senha (str): Senha para autenticação.

        Returns:
            bool: True se o login for bem-sucedido, False caso contrário.
        """
        if obj.cargo == 'Funcionario' or obj.cargo == 'Gerente':
            if obj.autenticacao(senha):
                print('login realizado com sucesso.')
                return True
            else:
                print('falha no login.')
                return False
        else:
            print('obj não autenticado.')
            return False


class Funcionario(Pessoa, Autenticacao):
    """
    Classe que define um funcionário, uma subclasse de Pessoa e Autenticacao.

    Atributos:
        cargo (str): Cargo do funcionário.
        _senha_funcionario (int): Senha do funcionário para autenticação.

    Métodos:
        ver_pessoa(): Visualiza informações do funcionário.
        autenticacao(senha): Implementação da autenticação para funcionário.
    """
    def __init__(self, nome, cpf):
        """
        Inicializa uma nova instância da classe Funcionario.

        Args:
            nome (str): Nome do funcionário.
            cpf (str): CPF do funcionário.
        """
        super().__init__(nome, cpf)
        self.cargo = 'Funcionario'
        self._senha_funcionario = randint(1, 10000)

    def ver_pessoa(self):
        """
        Visualiza informações do funcionário.
        """
        print(f'nome = {self._nome}\ncpf = {self._cpf}\ncargo = {self.cargo}\nsenha = {self._senha_funcionario}')

    def autenticacao(self, senha):
        """
        Implementação da autenticação para funcionário.

        Args:
            senha (str): Senha a ser verificada.

        Returns:
            bool: True se a senha for válida, False caso contrário.
        """
        return senha == self._senha_funcionario


class Gerente(Pessoa, Autenticacao):
    """
    Classe que define um gerente, uma subclasse de Pessoa e Autenticacao.

    Atributos:
        cargo (str): Cargo do gerente.
        _senha_gerente (int): Senha do gerente para autenticação.

    Métodos:
        ver_pessoa(): Visualiza informações do gerente.
        autenticacao(senha): Implementação da autenticação para gerente.
    """
    def __init__(self, nome, cpf):
        """
        Inicializa uma nova instância da classe Gerente.

        Args:
            nome (str): Nome do gerente.
            cpf (str): CPF do gerente.
        """
        super().__init__(nome, cpf)
        self.cargo = 'Gerente'
        self._senha_gerente = randint(1, 10000)
    
    def ver_pessoa(self):
        """
        Visualiza informações do gerente.
        """
        print(f'nome = {self._nome}\ncpf = {self._cpf}\ncargo = {self.cargo}\nsenha = {self._senha_gerente}')
    
    def autenticacao(self, senha):
        """
        Implementação da autenticação para gerente.

        Args:
            senha (str): Senha a ser verificada.

        Returns:
            bool: True se a senha for válida, False caso contrário.
        """
        return senha == self._senha_gerente
