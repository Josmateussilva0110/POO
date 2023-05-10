while True:
    value = int(input())
    if value < 0:
        break
    for i in range(1, value):
        value *= i
    print(f'{value}')
