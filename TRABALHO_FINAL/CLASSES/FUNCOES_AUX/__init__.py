from os import system
from time import sleep


def linha(tam=30):
    return '-' * tam


def cabecalho(txt, tam=30):
    print(linha(tam))
    print(txt.center(tam))
    print(linha(tam))


def menu(lista, txt='MENU PRINCIPAL'):
    print()
    cabecalho(txt)
    print()
    for i, v in enumerate(lista):
        print(f'[{i}] - {v}')
    print(linha())
    opc = leia_int('sua opção: ', 0, len(lista)-1)
    return opc


def limpa_tela(tempo=1):
    sleep(tempo)
    system('cls')


def leia_int(pergunta, inicio=0, fim=0):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
            else:
                print(f'valor invalido digite entre {inicio} e {fim}')
        except (ValueError, TypeError):
           print('ERRO, digite um valor valido')
        except (KeyboardInterrupt):
            print('usuario preferiu não digitar esse número')
            return 0


def ler_str(pergunta):
    while True:
        try:
            saida = input(pergunta)
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse valor')
            return ''
        else:
            if saida.replace(' ', '').isalpha():
                return saida
            else:
                print('ERRO, digite um valor válido contendo apenas letras.')



def ler_int(num):
    while True:
        try:
            n = int(input(num))
            if n >= 0:
                return n
            else:
                print('valor invalido.')
        except (ValueError, TypeError):
            print('ERRO, digite um número valido')
        except KeyboardInterrupt:
            print('usuario preferiu não digitar esse número')
            return 0


def ler_float(num):
    while True:
        try:
            n = float(input(num))
            if n > 0:
                return n
            else:
                print('valor invalido.')
        except (ValueError, TypeError):
            print('ERRO, digite um número valido')
        except KeyboardInterrupt:
            print('usuario preferiu não digitar esse número')
            return 0


def print_pessoas(conta, type=0):
    if type == 1:
        cabecalho('GERENTES:', 63)
    elif type == 2:
        cabecalho('FUNCIONARIOS:', 63)
    print('{:<8} {:<25} {:<10}'.format('CPF', 'NOME', 'CARGO'))
    print(linha(63))
    for cpf, funcionario in conta.items():
        nome_formatado = funcionario.nome.ljust(20)  
        cargo_formatado = funcionario.cargo.ljust(15) 
        print('{:<8} {:<25} {:<10}'.format(cpf, nome_formatado, cargo_formatado))
    print(linha(63))
