base = int(input())
expoente = int(input())
total = 1
for _ in range(expoente):
    total *= base
print(f'{total}')
