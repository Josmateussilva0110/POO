def contatenar(lista1, lista2):
    ans = list()
    for i in lista1:
        ans.append(i)
    for i in lista2:
        ans.append(i)
    return ans


values1 = list()
values2 = list()

print('lista1: ')
for i in range(5):
    value = int(input())
    values1.append(value)
print('lista2:')
for i in range(5):
    value = int(input())
    values2.append(value)
ans = contatenar(values1, values2)
print(ans)
