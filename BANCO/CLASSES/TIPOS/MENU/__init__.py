from os import system
from time import sleep


def linha(tam=30):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista, txt='MENU PRINCIPAL'):
    print()
    cabecalho(txt)
    print()
    for i, v in enumerate(lista):
        print(f'{i} - {v}')
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
        except (ValueError, TypeError):
            print('ERRO, digite um número valido')
        except KeyboardInterrupt:
            print('usuario preferiu não digitar esse número')
            return 0
        else:
            return n


def ler_float(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('ERRO, digite um número valido')
        except KeyboardInterrupt:
            print('usuario preferiu não digitar esse número')
            return 0
        else:
            return n


def print_contas(conta):
        for i, v in conta.items():
            print(linha())
            print('DADOS:')
            print(f'cpf = {i}\nnumero da conta = {v._numero}\nsaldo = {v._saldo:.2f}\nnome = {v._titular.nome}\ntipo de conta = {v._tipo}')
            print(linha())
