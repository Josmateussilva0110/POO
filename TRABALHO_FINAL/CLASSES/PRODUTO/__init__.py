class Produto():
    """
    Representa um produto disponível no estoque.

    A classe Produto possui atributos para armazenar informações sobre o produto,
    como código, nome, preço e quantidade em estoque.

    Atributos:
        _codigo (int): O código único do produto.
        _nome (str): O nome do produto.
        _preco (float): O preço unitário do produto.
        _quant (int): A quantidade disponível em estoque.

    Metodos:
        __str__: Retorna uma representação em formato de string do produto.

    """

    def __init__(self, codigo, nome, preco, quant):
        """
        Inicializa uma nova instância da classe Produto.

        Argumentos:
            codigo (int): O código único do produto.
            nome (str): O nome do produto.
            preco (float): O preço unitário do produto.
            quant (int): A quantidade disponível em estoque.
        """
        self._codigo = codigo
        self._nome = nome
        self._preco = preco
        self._quant = quant

    def __str__(self):
        """
        Retorna uma representação em formato de string do produto.

        Retorno:
            str: Uma string contendo informações sobre o produto.
        """
        return f'{self._codigo}\n{self._nome}\n{self._preco}\n{self._quant}'
