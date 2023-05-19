value = int(input('valor: '))
bi = ''
if value == 0:
    bi = '0'
else:
    while value > 0:
        tot = value % 2
        bi = str(tot) + bi
        value = value // 2
print(f'binario = {bi}')
