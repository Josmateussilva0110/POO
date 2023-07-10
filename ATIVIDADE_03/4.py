class Controle_Remoto():
    def __init__(self, volume = '', canais = ''):
        self.volume = volume
        self.canais = canais

    def menu(self, lista):
        tam = len(lista)
        while True:
            print('-----MENU-----')
            for i, v in enumerate(lista):
                print(f'{i+1} - {v}')
            opc = int(input('sua opcao: '))
            if opc >= 1 and opc <= tam:
                break
            else:
                print('opcao invalida!')
        return opc
    
    def controlar_volume(self):
        obj = Controle_Remoto()
        opc = obj.menu(['aumentar', 'diminuir'])
        if opc == 1:
            self.volume +=1
            print('volume aumentado.')
        elif opc == 2:
            self.volume -= 1
            print('volume diminuido.')
    
    def trocar_canais(self):
        print(f'canal atual = {self.canais}')
        obj = Controle_Remoto()
        opc = obj.menu(['aumentar canal', 'dininuir canal', 'escolher um'])
        if opc == 1:
            self.canais += 1
            print('canal aumentado.')
        if opc == 2:
            self.canais -= 1
            print('canal diminuido.')
        if opc == 3:
            numero = int(input('numero do canal: '))
            self.canais = numero
            print('canal alterado.')
    
    def consultar_valor(self):
        print(f'volume da televisao = {self.volume}')
        print(f'a tv esta no canal = {self.canais}')


class Televisao():
    def __init__(self):
        self.aux = Controle_Remoto(0, 1)




lista = ['sair', 'controlar volume', 'trocar de canais', 'consultar valor']
controle = Televisao()
while True:
    op = controle.aux.menu(lista)
    if op == 1:
        break
    if op == 2:
        controle.aux.controlar_volume()
    if op == 3:
        controle.aux.trocar_canais()
    if op == 4:
        controle.aux.consultar_valor() 
