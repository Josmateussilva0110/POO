def fatorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


num = int(input('valor: '))
result = fatorial(num)
print(f'fatorial de {num} é {result}')
