ganha_h = float(input())
horas_trabalhadas = float(input())
salario_bruto = ganha_h * horas_trabalhadas
inss = (8/ 100) * salario_bruto
sindicato = (5 / 100) * salario_bruto
salario_liquido = (13 /100) * salario_bruto
print(f'salario Bruto: {salario_bruto:.2f} R$')
print(f'inss: {inss:.2f}')
print(f'sindicato: {sindicato:.2f}')
print(f'salario liquido: {salario_liquido}')
