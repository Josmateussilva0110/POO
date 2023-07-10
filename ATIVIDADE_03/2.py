class Pessoa():
     def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura


class Agenda():
    def __init__(self):
        self.pessoas = list()
    
    def armazenar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)
        return len(self.pessoas)


    def imprimir(self):
        for i in self.pessoas:
            print(f'idade = {i.idade}')
            print(f'nome = {i.nome}')
            print(f'altura = {i.altura}')
    

    def buscar_pessoa(self, nome):
        valid = False
        for i in self.pessoas:
            if i.nome in nome:
                print(f'idade = {i.idade}')
                print(f'nome = {i.nome}')
                print(f'altura = {i.altura}')
                valid = True
                break
        if not valid:
            print('nome nao encontrado.')
    

    def remover_pessoa(self, nome):
        j = 0
        index = -1
        for i in self.pessoas:
            if i.nome in nome:
                index = j
                break
            j+=1
        if index != -1:
            del self.pessoas[index]
            print('nome removido.')
        else:
            print('nome nao encontrado.')
        

agenda = Agenda()
i = 0
while True:
    print(f'pessoa {i+1}:')
    nome = input('nome: ')
    idade = int(input('idade: '))
    altura = float(input('altura: '))
    pessoa = Pessoa(nome, idade, altura)
    ans = agenda.armazenar_pessoa(pessoa) 
    if ans == 10:
        break
    i+= 1
agenda.imprimir()
name = input('nome que deseja buscar: ')
agenda.buscar_pessoa(name)
name2 = input('nome que deseja remover: ')
agenda.remover_pessoa(name2)
agenda.imprimir()
