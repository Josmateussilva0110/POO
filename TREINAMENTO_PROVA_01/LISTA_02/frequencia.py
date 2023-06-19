dados = dict()
lista = list()

while True:
    n = int(input())
    if n == 0:
        break
    lista.append(n)


for i in lista:
    if i in dados:
        dados[i] += 1
    else:
        dados[i] = 1

for index, value in dados.items():
    print(f'{index} - {value}')
