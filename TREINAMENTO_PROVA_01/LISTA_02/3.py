def cont(dados):
    cont = sun = 0
    for value in dados.values():
        sun += value[1]
    median = sun / 5
    print(f'media = {median}')
    for value in dados.values():
        if value[0] > 13 and value[1] < median:
            cont += 1
    return cont


dados = dict()

for i in range(5):
    dados2 = list()
    age = int(input(f'idade do aluno {i+1}: '))
    dados2.append(age)
    altura = float(input('altura: '))
    dados2.append(altura)
    dados[i] = dados2

print(dados2)
ans = cont(dados)
print(ans)
