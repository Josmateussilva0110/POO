value = int(input('quantos valores: '))
t1 = 0
t2 = 1
print(f'{t1} {t2}', end=' ')
for i in range(3, value+1):
    t3 = t1 + t2
    print(f'{t3}',end=' ')
    t1 = t2 
    t2 = t3
