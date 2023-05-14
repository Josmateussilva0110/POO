size = int(input('montar a tabela de: '))
first = int(input('começa por: '))
end = int(input('termina em: '))
print(f'vou montar a tabela de {size} começando em {first} e terminado em {end}')
for i in range(first, end+1):
    print(f'{size} x {i} = {size * i}')
