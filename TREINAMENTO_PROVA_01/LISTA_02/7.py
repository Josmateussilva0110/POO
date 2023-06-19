sistemas = ['windows','unix','linux','netware','mac','outro']

escolhas = list()
while True:
    while True:
        choise = int(input())
        if 0 <= choise <= 6:
            break
    if choise == 0:
        break
    escolhas.append(choise)

dados = dict()

for i in escolhas:
    if i in dados:
        dados[i] += 1
    else:
        dados[i] = 1

sun = 0
porcentagem = list()
votos = list()

for value in dados.values():
    sun += value
    votos.append(value)

for value in dados.values():
    result = (value * 100) / sun
    porcentagem.append(result)

for i, sistema in enumerate(sistemas):
    print(f'{sistema} - {votos[i]} - {porcentagem[i]:.2f} %')

print(f'total = {sun}')
ind = votos.index(max(votos))
print(f'O Sistema Operacional mais votado foi o {sistemas[ind]}, com {max(votos)} votos, correspondendo a {porcentagem[ind]:.2f} dos votos.')
