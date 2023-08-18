from classes.tipos.menu import *
from classes.tipos.classe_cadastrar import *
from classes.tipos.classe_conta import *
from random import randint


conta_corrente = dict()
conta_poupanca = dict()
tota_contas = dict()
tota_seguros = dict()
pessoas = Salvar()
seguro = SeguroVida()

while True:
    lista = ['sair', 'cadastrar pessoa', 'criar conta', 'informacao do banco', 'modo usuario', 'calcular tribitacao']
    op = menu(lista)
    if op == 0:
        break
    #----------------------------------------------------------------
    if op == 1:
        nome = ler_str('nome: ')
        cpf = ler_int('cpf: ')
        aux = pessoas.buscar_pessoa(cpf)
        if aux is None:
            pessoa = Cadastrar_Cliente(nome, cpf)
            pessoas.armazenar(pessoa)
            print('pessoa cadastrada com sucesso.')
        else:
            print('cpf ja cadastrado.')
        limpa_tela()
    #-----------------------------------------------------------------

    if op == 2:
        if pessoas.conta_sem_cadastro():
            print('nao eh possivel criar conta\nbanco sem cadastro.')
        else:
            tipo = menu(['corrente', 'poupanca', 'seguro de vida', 'cancelar operacao'], 'TIPOS')
            #-----------------------------------------------------------------
            if tipo == 0:
                numero = randint(1, 1000)
                pessoas.imprimir()
                escolha = ler_int('digite o cpf da pessoa que deseja criar a conta: ')
                p = pessoas.buscar_pessoa(escolha)
                if p is not None:
                    if escolha not in conta_corrente:
                        conta_c = Conta_Corrente(numero, p)
                        conta_corrente[escolha] = conta_c
                        if escolha not in tota_contas:
                            tota_contas[escolha] = 1
                        else:
                            tota_contas[escolha] +=1
                        print('conta corrente criada com sucesso.')
                    else:
                        print('ERRO, pessoa ja tem conta.')
                else:
                    print('pessoa nao encontrada')

            #-----------------------------------------------------------------
            if tipo == 1:
                numero = randint(1, 1000)
                pessoas.imprimir()
                escolha = ler_int('digite o cpf da pessoa que deseja criar a conta: ')
                p = pessoas.buscar_pessoa(escolha)
                if p is not None:
                    if escolha not in conta_poupanca:
                        conta_p = Conta_Poupanca(numero, p)
                        conta_poupanca[escolha] = conta_p
                        if escolha not in tota_contas:
                            tota_contas[escolha] = 1
                        else:
                            tota_contas[escolha] +=1
                        print('conta poupanca criada com sucesso.')
                    else:
                        print('ERRO, pessoa ja tem conta.')
                else:
                    print('pessoa nao encontrada')
            if tipo == 2:
                while True:
                    op = menu(['criar seguro', 'exibir todos os seguros', 'sair'])
                    if op == 0:
                        valor_mensal = ler_float('valor mensal: ')
                        valor_total = ler_float('valor total: ')
                        pessoas.imprimir()
                        cpf_seguro = ler_int('cpf que deseja criar o seguro: ')
                        pess = pessoas.buscar_pessoa(cpf_seguro)
                        if pess is not None:
                            seguro.criar_seguro(pess, valor_mensal, valor_total)
                            if cpf_seguro not in tota_seguros:
                                tota_seguros[cpf_seguro] = 1
                            else:
                                tota_seguros[cpf_seguro] += 1
                            print('seguro criado com sucesso.')
                        else:
                            print('pessoa nao encontrada')
                    if op == 1:
                        seguro.imprimir_seguros()
                        sleep(2)
                    if op == 2:
                        print('operacao cancelada.')
                        break
                    limpa_tela()
            if tipo == 3:
                print('operacao cancelada.')
        limpa_tela()
    if op == 3:
        pessoas.imprimir(tota_contas, tota_seguros, True)
    
    if op == 4:
        if pessoas.conta_sem_cadastro():
            print('nao eh possivel entrar nesse modo\nbanco sem cadastro.')
        else:
            opc = ler_int('cpf da pessoa que deseja fazer a operacao: ')
            limpa_tela()
            if opc in conta_corrente and opc in conta_poupanca:
                qual = menu(['corrente', 'poupanca', 'cancelar'], 'QUAL CONTA DESEJA FAZER A OPERACAO')
                if qual == 0:
                        limpa_tela(0.5)
                        while True:
                            operacoes = menu(['sacar', 'depositar', 'ver saldo', 'extrato', 'informacoes da conta', 'transferir', 'sair'], 'CONTA CORRENTE')
                            if operacoes == 6:
                                break
                            if operacoes == 5:
                                print_contas(conta_corrente)
                                cp = ler_int('digite o cpf da conta de destino: ')
                                if cp != opc:
                                    conta_destino = conta_c.buscar_conta(cp, conta_corrente)
                                    if conta_destino is not None:
                                        valor = ler_float('valor que deseja transferir: ')
                                        conta_corrente[opc].transferir(valor, conta_destino)
                                    else:
                                        print('Conta destino não encontrada.')
                                else:
                                    print('ERRO, nao pode fazer transferencia para a mesma conta')
                            conta_corrente[opc].decidir_operacao(conta_corrente[opc], operacoes)
                if qual == 1:
                    limpa_tela(0.5)
                    while True:
                        operacoes = menu(['sacar', 'depositar', 'ver saldo', 'extrato', 'informacoes da conta', 'transferir', 'sair'], 'CONTA POUPANCA:')
                        if operacoes == 6:
                            break
                        if operacoes == 5:
                            print_contas(conta_poupanca)
                            cp = ler_int('digite o cpf da conta de destino: ')
                            if cp != opc:
                                conta_destino = conta_p.buscar_conta(cp, conta_poupanca)
                                if conta_destino is not None:
                                    valor = ler_float('valor que deseja transferir: ')
                                    conta_poupanca[opc].transferir(valor, conta_destino)
                                else:
                                    print('Conta destino não encontrada.')
                            else:
                                print('ERRO, nao pode fazer transferencia para a mesma conta')
                        conta_poupanca[opc].decidir_operacao(conta_poupanca[opc], operacoes)
                if qual == 2:
                    print('operacao cancelada.')
                limpa_tela(0.5)
            elif opc in conta_corrente:
                    limpa_tela(0.5)
                    while True:
                        operacoes = menu(['sacar', 'depositar', 'ver saldo', 'extrato', 'informacoes da conta', 'transferir', 'sair'], 'CONTA CORRENTE:')
                        if operacoes == 6:
                            break
                        if operacoes == 5:
                            print_contas(conta_corrente)
                            cp = ler_int('digite o cpf da conta de destino: ')
                            if cp != opc:
                                conta_destino = conta_c.buscar_conta(cp, conta_corrente)
                                if conta_destino is not None:
                                    valor = ler_float('valor que deseja transferir: ')
                                    conta_corrente[opc].transferir(valor, conta_destino)
                                else:
                                    print('Conta destino não encontrada.')
                            else:
                                print('ERRO, nao pode fazer transferencia para a mesma conta')
                        conta_corrente[opc].decidir_operacao(conta_corrente[opc], operacoes)
            elif opc in conta_poupanca:
                    limpa_tela(0.5)
                    while True:
                        operacoes = menu(['sacar', 'depositar', 'ver saldo', 'extrato', 'informacoes da conta', 'transferir', 'sair'], 'CONTA POUPANCA:')
                        if operacoes == 6:
                            break
                        if operacoes == 5:
                            print_contas(conta_poupanca)
                            cp = ler_int('digite o cpf da conta de destino: ')
                            if cp != opc:
                                conta_destino = conta_p.buscar_conta(cp, conta_poupanca)
                                if conta_destino is not None:
                                    valor = ler_float('valor que deseja transferir: ')
                                    conta_poupanca[opc].transferir(valor, conta_destino)
                                else:
                                    print('Conta destino não encontrada.')
                            else:
                                print('ERRO, nao pode fazer transferencia para a mesma conta')
                        conta_poupanca[opc].decidir_operacao(conta_poupanca[opc], operacoes)
    if op == 5:
        print('em breve')
