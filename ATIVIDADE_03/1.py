from datetime import date

class Pessoa():
    def __init__(self, nome, nasc, altura):
        self._nome = nome
        self._nasc = nasc
        self._altura = altura
        self._idade = ''

    @property
    def nome(self):
        return self._nome

    @property
    def nasc(self):
        return self._nasc
    # get
    @property
    def altura(self):
        return self._altura
    
    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome):
        if nome.isalpha():
            self._nome = nome
        else:
            print('Nome invalido.')
            self._nome = None

    @nasc.setter
    def nasc(self, valor):
        if self._nasc[0] > 0:
            self._nasc.append(valor)
        else:
            self._nasc.append(0)

    @altura.setter
    def altura(self, valor):
        if isinstance(valor, float):
            self._altura = valor
        else:
            print('altura invalida.')
            self._altura = 0

    def calcular_idade(self):
        if self._nasc[0] != 0:
            data = date.today()
            dat = [data.year, data.month, data.day]
            dat.reverse()
            self._idade = dat[2] - self._nasc[2]
            if self._nasc[1] > dat[1]:
                self._idade -= 1
            elif self._nasc[1] == dat[1] and self._nasc[0] < dat[0]:
                self._idade -= 1
        else:
            print('nao foi possivel calcular sua idade.')
            self._idade = 0
        return self._idade

    def imprimir(self):
        print('DADOS:')
        print(f'Nome: {self._nome}')
        print(f'Nascimento: {self._nasc}')
        print(f'Altura: {self._altura:.2f}')
        print(f'Idade: {self._idade}')


data = list()

nome = input('Seu nome: ')
dia = int(input('dia: '))
data.append(dia)
mes = int(input('mes: '))
data.append(mes)
ano = int(input('ano: '))
data.append(ano)
altura = float(input('Sua altura: '))
print(data)
pessoa = Pessoa(nome, data, altura)
ans = pessoa.calcular_idade()
print(f'Sua idade é {ans}')
pessoa.imprimir()
