dados = dict()


def calcular(dados):
    ans = dict()
    for index, value in dados.items():
        ans[index] = sum(value) / len(value)
    
    media = 0
    for index, value in ans.items():
        if value > media:
            name = index
    return ans, name



for _ in range(3):
    name = input()
    notas = list(map(int, input().split(' ')))
    dados[name] = notas
    ans = calcular(dados)
print(ans[0])
print(ans[1])
