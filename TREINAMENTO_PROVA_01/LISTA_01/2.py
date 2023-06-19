def istrianreg(a, b, c):
    if c ** 2 == (a ** 2 + b ** 2):
        return True
    else:
        return False
    


lado1, lado2, lado3 = map(int, input().split(' '))
if lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado2 + lado1):
    print('nao forma triangulo')
else:
    print('eh possivel formar triangulo')
    if lado1 == lado2 and lado2 == lado3:
        print('triangulo equilatero')
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print('triangulo escaleno')
    else:
        print('isoceles')
    ans = istrianreg(lado1, lado2, lado3)
    if ans:
        print('triangulo retangulo')
    else:
        print('nao eh triangulo retangulo')
