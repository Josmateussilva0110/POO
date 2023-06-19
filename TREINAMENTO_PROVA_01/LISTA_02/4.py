perguntas = ['telefonou para a vitima',
           'esteve no local do crime',
           'mora perto da vitima',
           'devia para a vitima',
           'ja trabalhou com a vitima']

cont = 0
for i in perguntas:
    print(i)
    choise = int(input('sua opcao (1-sim/0-nao): '))
    if choise:
        cont +=1
if cont == 2:
    print('suspeito')
elif 3 <= cont <= 4:
    print('cumplice')
elif cont == 5:
    print('assassino')
else:
    print('inicente')
