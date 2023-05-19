while True:
    tipo = int(input('escolha:\n1- triangulo\n2- quadrado\n3- circulo\n4- sair: \n'))
    if tipo == 4:
        break
    if tipo == 1:
        base = int(input('infrome a base: '))
        altura = int(input('altura: '))
        area = (base * altura) / 2
    if tipo == 2:
        lado = int(input('informe o valor do lado: '))
        area = lado ** 2
    if tipo == 3:
        raio = int(input('informe o raio do circulo: '))
        area = 3.14159 * (raio ** 2)
    print(f'area = {area}')
