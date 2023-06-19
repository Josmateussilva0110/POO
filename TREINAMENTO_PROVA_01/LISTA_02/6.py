dado = dict()

while True:
    saltos = list()
    name = input('nome: ')
    if name == ' ':
        break
    for i in range(5):
        salto = float(input(f'salto {i+1}: '))
        saltos.append(salto)
    dado[name] = saltos

medias = list()
for value in dado.values():
    media = sum(value) / len(value)
    medias.append(media)

cont = 0
print('resultado final:')
for index, value in dado.items():
    print(f'atleta: {index}\nsaltos: {value}')
    print(f'media dos saltos: {medias[cont]}')
    cont += 1
