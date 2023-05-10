litros = float(input())
tipo = input()
if tipo == 'A':
    if litros < 20:
        des = litros - (litros * 3 / 100)
    else:
        des = litros - (litros * 5 / 100)
    total = des * 3.45
if tipo == 'G':
    if litros < 20:
        des = litros - (litros * 4 / 100)
    else:
        des = litros - (litros * 6 / 100)
    total = des * 4.53
print(f'valor a ser pago: {total:.2f}')
