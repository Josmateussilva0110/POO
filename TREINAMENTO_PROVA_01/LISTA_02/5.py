salaries = []

for i in range(5):
    salary = float(input(f'salario {i+1}: '))
    salaries.append(salary)

new_salaries = []

for i in salaries:
    result = 200 + (i * 0.09)
    new_salaries.append(result)

print(new_salaries)
cont = {}

for i in new_salaries:
    if i in cont:
        cont[i] += 1
    else:
        cont[i] = 1

for salary, count in cont.items():
    print(f'{salary} - {count}')
