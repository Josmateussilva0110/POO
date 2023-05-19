preco_ingresso_inicial = 5.00
preco_ingresso_final = 1.00
intervalo_preco_ingresso = 0.50

lucro_maximo = 0
preco_ingresso_lucro_maximo = 0
qtd_ingressos_lucro_maximo = 0

preco_ingresso = preco_ingresso_inicial
while preco_ingresso >= preco_ingresso_final:
    qtd_ingressos = 120 + (preco_ingresso_inicial - preco_ingresso) * 52
    lucro = (preco_ingresso * qtd_ingressos) - 200
    print(f'Preço do ingresso: {preco_ingresso}')
    print(f'Quantidade de ingressos vendidos: {qtd_ingressos}')
    print(f'Lucro esperado:{lucro}')
    print()
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_ingresso_lucro_maximo = preco_ingresso
        qtd_ingressos_lucro_maximo = qtd_ingressos
    preco_ingresso -= intervalo_preco_ingresso
print(f'Lucro máximo esperado:{lucro_maximo}')
print(f'Preço do ingresso correspondente ao lucro máximo:{preco_ingresso_lucro_maximo}')
print(f'Quantidade de ingressos vendidos para o lucro máximo: {qtd_ingressos_lucro_maximo}')
