class Elevador():
    def __init__(self, terreo, tot_andares, capacidade, qnt_pessoas):
        self._terreo = terreo
        self._tot_andares = tot_andares
        self._capacidade = capacidade
        self._qnt_pessoas = qnt_pessoas
    
    @property
    def terreo(self):
        return self._terreo

    @property
    def tot_andares(self):
        return self._terreo

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def qnt_pessoas(self):
        return self._qnt_pessoas


    @terreo.setter
    def terreo(self, valor):
        if valor > 0:
            self._terreo = valor
        else:
            print('valor invalido.')
    
    @tot_andares.setter
    def tot_andares(self, valor):
        if valor > 0:
            self._tot_andares = valor
        else:
            print('valor invalido.')
    
    @capacidade.setter
    def capacidade(self, valor):
        if valor > 0:
            self._tot_andares = valor
        else:
            print('valor invalido.')
    
    @qnt_pessoas.setter
    def qnt_pessoas(self, valor):
        if valor > 0:
            self._tot_andares = valor
        else:
            print('valor invalido.')

    def inicializa(self, capacidade, tot_andares):
        print(f'o elevador tem capacidade de {capacidade}')
        print(f'o predio tem {tot_andares-1} andares mais o terreo')

    def entra(self, capacidade):
        if self._qnt_pessoas < capacidade:
            self._qnt_pessoas += 1
            print('pessoa dentro.')
            print(f'quantidade de pessoas {self._qnt_pessoas}')
        else:
            print('elevador cheio')
    
    def sai(self):
        if self._qnt_pessoas > 0:
            self._qnt_pessoas -= 1
            print('pessoa saiu.')
            print(f'quantidade de pessoas {self._qnt_pessoas}')
        else:
            print(f'elevador esta vazio.')


    def menu(self, lista):
        for i, v in enumerate(lista):
            print(f'{i} - {v}')
    

    def sobe(self):
        if self._terreo >= self._tot_andares:
            print(f'ja esta no ultimo andar.')
        else:
            self._terreo +=1 
            print(f'subiu {self._terreo} andar.')
    

    def descer(self):
        if self._terreo > 0:
            self._terreo -= 1
            print('ja esta no terreo.')
            print(f'voce desceu para o andar {self._terreo}.')
        else:
            print('elevador ja esta no terreo.')


lista = ['sair', 'entrar', 'sair do elevador', 'sobe', 'descer']
ele = Elevador(0, 5, 3, 0)
ele.inicializa(ele._capacidade, ele._tot_andares)
while True:
    ele.menu(lista)
    op = int(input('sua opcao: '))
    if op == 0:
        break
    if op == 1:
        ele.entra(ele.capacidade)
    if op == 2:
        ele.sai()
    if op == 3:
        ele.sobe()
    if op == 4:
        ele.descer()
