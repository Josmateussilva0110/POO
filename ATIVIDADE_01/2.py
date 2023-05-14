peso = float(input())
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print(f'{excesso}')
print(f'{multa:.2f}')
