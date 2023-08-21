from tipos.funcoes_aux import *
import math

class Comercial():
    """
    Classe que representa uma compra comercial.

    Atributos:
        _codigo (int): Código do produto.
        _qnt (int): Quantidade do produto.
        _produtos (dict): Dicionário de produtos.
        _total_compra (float): Valor total da compra.

    Métodos:
        calcular_compra(): Calcula o valor total da compra.
        calcular_troco(cliente, total_compra): Calcula o troco para o cliente.
        ler_cartao(txt): Lê o número do cartão do cliente.
        calcular_parcelas(total_compra): Calcula o número de parcelas baseado no valor total da compra.
    """

    def __init__(self, codigo, qnt, produtos):
        """
        Inicializa uma nova instância da classe Comercial.

        Args:
            codigo (int): Código do produto.
            qnt (int): Quantidade do produto.
            produtos (dict): Dicionário de produtos.
        """
        self._codigo = codigo
        self._qnt = qnt
        self._produtos = produtos
        self._total_compra = 0.0

    def calcular_compra(self):
        """
        Calcula o valor total da compra.

        Returns:
            float: Valor total da compra.
        """
        for i, v in self._produtos.items():
            if i == self._codigo:
                self._total_compra += (v._preco * self._qnt)
                break
        return self._total_compra

    def calcular_troco(self, cliente, total_compra):
        """
        Calcula o troco para o cliente.

        Args:
            cliente (float): Valor pago pelo cliente.
            total_compra (float): Valor total da compra.

        Returns:
            float: Valor do troco.
        """
        troco = 0
        if cliente > total_compra:
            troco = cliente - total_compra
        else:
            while cliente < total_compra:
                print(f'total da compra = {total_compra:.2f}')
                cliente = ler_float('valor insuficiente.\ntente novamente: ')
                limpa_tela()
                if cliente >= total_compra:
                    troco = cliente - total_compra
        return troco

    def ler_cartao(self, txt):
        """
        Lê o número do cartão do cliente.

        Args:
            txt (str): Mensagem de entrada.

        Returns:
            int: Número do cartão lido.
        """
        while True:
            valores = ler_int(txt)
            if len(str(valores)) == 6:
                break
            else:
                print('erro na leitura\ndigite novamente.')

    def calcular_parcelas(self, total_compra):
        """
        Calcula o número de parcelas baseado no valor total da compra.

        Args:
            total_compra (float): Valor total da compra.

        Returns:
            int: Número de parcelas calculado.
        """
        valores = []
        max_parcelas = 5  # Quantidade máxima de parcelas

        for parcela in range(1, min(max_parcelas, math.ceil(total_compra / 50)) + 1):
            valores.append(parcela)

        op = menu(valores, 'PARCELAS:')
        return op
