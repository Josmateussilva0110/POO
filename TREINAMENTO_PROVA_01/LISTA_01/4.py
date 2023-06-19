vogais = ['a', 'e', 'i', 'o', 'u']


def is_consoante(string):
    if string.lower() not in vogais:
        return True
    else:
        return False


result = list()
string = input()
ans = list(string)
cont = 0
for i in ans:
    if is_consoante(i) and i != ' ':
        result.append(i)
        cont += 1
print(f'consoantes da string:')
consoantes = ' '.join(result)
print(consoantes)
print(f'quatidade de consoantes = {cont}')
