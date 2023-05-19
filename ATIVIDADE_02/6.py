def primo(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

value = int(input('valor: '))
print(primo(value))
first = int(input('comeco: '))
end = int(input('fim: '))
cont = 0
for i in range(first, end):
    if(primo(i)):
        print(i)
        cont += 1
if not cont:
    print('Nao existe nenhum número primo dentro desse intervalo.')
