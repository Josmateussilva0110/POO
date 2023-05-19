def fatorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def arranjo(n, p):
    a = fatorial(n) / fatorial((n - p))
    return a


def combinacao(n, r):
    c = fatorial(n) / ((fatorial(r)) * (fatorial(n - r)))
    return c


n = int(input('valor: '))
a = arranjo(n, 2)
c = combinacao(n, 2)
print(f'arranjo = {a}')
print(f'combinacao = {c}')
