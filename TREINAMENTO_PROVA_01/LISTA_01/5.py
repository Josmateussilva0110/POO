dados = dict()
names = list()
size = int(input('quantidade de alunos: '))
for i in range(size):
    name = input(f'nome do aluno {i+1}: ')
    notes = list(map(float, input(f'as quatros notas: ').split(' ')))
    dados[name] = sum(notes) / len(notes)
for index, value in dados.items():
    if value > 7.0:
        names.append(index)
print(dados)
print('alunos com media maior que 7:')
for i in names:
    print(i, end=' ')
