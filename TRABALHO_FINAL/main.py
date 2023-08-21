from tipos.class_produtos import *
from tipos.class_armazenar import *
from tipos.class_pessoa import *
from tipos.funcoes_aux import *
from tipos.class_comercial import *
from random import randint
#------------‐---------------------------------------------------------

dados = Armazenar()
gerentes = dict()
funcionarios = dict()
produtos = dict()
while True:
	sistema = Sistema_interno()
	op = menu(['sair', 'cadastrar pessoa', 'cadastrar produtos', 'exibir informacoes', 'modo comercial'])
	if op == 0:
		break
	elif op == 1:
		nome = ler_str('nome da pessoa: ')
		cpf = ler_int('cpf: ')
		limpa_tela(0.5)
		tipo = menu(['sair', 'gerente', 'funcionario'],'CARGO:')
		if tipo == 0:
			break

		elif tipo == 1:
			gerente = Gerente(nome, cpf)

			if gerente._senha_gerente not in gerentes and gerente._senha_gerente not in funcionarios:
				gerentes[gerente._senha_gerente] = gerente
				dados.armazenar_pessoas(gerente)
				print(f'sua senha eh = {gerente._senha_gerente}')
				print('pessoa cadastrada com sucesso.')
			else:
				print('pessoa ja cadastrada em outro cargo.')
			limpa_tela()
		elif tipo == 2:
			funcionario = Funcionario(nome, cpf)
			if cpf not in funcionarios and cpf not in gerentes:
				funcionarios[cpf] = funcionario
				print(f'sua senha eh = {funcionario._senha_funcionario}')
				dados.armazenar_pessoas(funcionario)
				print('pessoa cadastrada com sucesso.')
			else:
				print('pessoa ja castrada em outro cargo.')
			limpa_tela()
	elif op == 2:
		if not gerentes:
			print('nao pode cadastrar produtos.\ncadastre um gerente.')
		else:
			limpa_tela(0.5)
			senha_g = ler_int('senha do gerente: ')
			if senha_g in gerentes:
				gerente = gerentes[senha_g]
				certo = sistema.login(gerente, senha_g)
				if certo:
					limpa_tela(0.5)
					while True:
						cabecalho('INFORMACOES DO PRODUTO:')
						codi = randint(1, 100000)
						nome_produto = ler_str('nome do produto: ')
						preco_produto = ler_float('preco: ')
						quant_produto = ler_int('quantidade: ')
						if codi not in produtos:
							produto = Produto(codi, nome_produto, preco_produto, quant_produto)
							produtos[codi] = produto
							dados.armazenar_produtos(produto)
						else:
							print('produto ja cadastrado.')
						limpa_tela(0.5)
						contin = menu(['sair', 'continuar'], 'CONTINUAR OPERACAO:')
						if contin == 0:
							break
						limpa_tela(0.5)
			else:
				print('falha na autenticacao.')
			#limpa_tela()
	elif op == 3:
		while True:
			quais = menu(['sair', 'pessoas', 'produtos'], 'OPCAO PARA EXIBIR:')
			if quais == 0:
				break
			elif quais == 1:
				while True:
					tipo = menu(['sair','gerentes', 'funcionarios'], 'CARGO:')
					if tipo == 0:
						break
					if tipo == 1:
						dados.imprimir_pessoa(dados._gerentes)
					elif tipo == 2:
						dados.imprimir_pessoa(dados._funcionarios)
			elif quais == 2:
				dados.imprimir_produtos()
		limpa_tela(0.5)
	elif op == 4:
		if not produtos:
			print('nao pode entrar\nnao ah produtos cadastrados.')
		else:
			limpa_tela(0.5)
			senha_f = ler_int('senha do funcionario: ')
			funcionarios_encontrados = None
			for func in funcionarios.values():
				if func.autenticacao(senha_f):
					funcionarios_encontrados = func
					break
			if funcionarios_encontrados is not None:
				certo_f = sistema.login(funcionarios_encontrados, senha_f)
				if certo_f:
					limpa_tela(0.5)
					while True:
						q_produtos = 0
						compra_total = 0.0
						while True:
							print(f'quantidade de produtos passados = {q_produtos}')
							dados.imprimir_produtos()
							codi_produto = ler_int('codigo do produto (0- sair): ')
							if codi_produto == 0:
								break
							dados.buscar_produto(codi_produto)
							prod_encontrado = dados.buscar_produto(codi_produto)
							if prod_encontrado != None:
								q_produtos +=1
								limpa_tela(0.5)
								dados.imprimir_um_produto(prod_encontrado)
								if prod_encontrado._quant <= 0:
									print('nao ah produtos no estoque.')
								else:
									# aqui
									while True:
										qnt_produto = ler_int('quantidade: ')
										if qnt_produto <= prod_encontrado._quant:
											prod_encontrado._quant -= qnt_produto
											break
										else:
											print('ERRO, o produto nao tem essa quantidade em estoque.')
											print('digite um valor menor.')
								limpa_tela(0.5)
								comercio = Comercial(codi_produto, qnt_produto, produtos)
								compra_total += comercio.calcular_compra()
							else:
								print('produto nao encontrado.')
								limpa_tela()
						limpa_tela(0.5)
						print(f'total da compra = {compra_total:.2f}')
						if compra_total > 0:
							opcs = menu(['sair', 'a vista', 'debito', 'credito'],'OPCOES')
							if opcs == 0:
								print('operacao cancelada.')
							elif opcs == 1:
								valor_pagar = ler_float('insira o valor a pagar: ')
								troco = comercio.calcular_troco(valor_pagar, compra_total)
								print(f'troco = {troco:.2f}')
								print('compra finalizada com sucesso.')
							elif opcs == 2:
								comercio.ler_cartao('codigo do cartao (6- digitos): ')
								comercio.ler_cartao('senha: (6- digitos): ')
								print('compra realizada com sucesso.')
								limpa_tela()
							elif opcs == 3:
								sub_total = 0
								limpa_tela(0.5)
								print(f'total da compra = {compra_total:.2f}')
								qnt_parcelas = comercio.calcular_parcelas(compra_total)
								comercio.ler_cartao('codigo do cartao (6- digitos): ')
								comercio.ler_cartao('senha: (6- digitos): ')
								qnt_parcelas += 1
								sub_total = compra_total / qnt_parcelas
								print(f'o valor {compra_total:.2f} ficou dividido em {qnt_parcelas}X')
								print(f'total da compra parcelada = {sub_total:.2f}')
								print('compra realizada com sucesso.')
								#limpa_tela()
						else:
							print('operacao cancelada.')
						sair = menu(['sair', 'continuar'], 'DESEJA SAIR DO MODO COMERCIAL:')
						if sair == 0:
							break
						limpa_tela(0.5)
				else:
					print('falha na autenticacao.')
			else:
				print('pessoa nao encontrada.')
