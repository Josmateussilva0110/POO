def quadrado(lista):
    ans = list()
    for i in lista:
        result = i ** 2
        ans.append(result)
    return ans



values = [1,2,4,6]
ans = quadrado(values)
print(ans)
