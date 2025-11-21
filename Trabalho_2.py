'''Faça um programa para controlar os assentos disponíveis nos ônibus de uma empresa
de transporte rodoviário de passageiros. Cada linha tem um conjunto de horários
diários de partida de ônibus. Cada ônibus suporta até 20 passageiros: assentos de 1 até
20, onde os ímpares são nas janelas.
 ((Os dados de cada linha são:
o Cidade de origem
o Cidade de destino
o Horário de partida (hora:minuto)
o Valor da passagem))
 Cada linha tem ônibus partindo todos os dias. Portanto, as informações de cada ônibus
são:
((o Data da partida (dia/mês/ano)
o Assentos disponíveis))
 O sistema deve permitir:
o Cadastro de linhas: inserir, remover e alterar.
o Consultar todos os horários disponíveis para uma determinada cidade.
o Consultar os assentos disponíveis no ônibus, informando a cidade de destino,
horário e data. A data deve ser inferior a 30 dias, contados a partir da data atual.
o Após uma consulta de assento disponível, o sistema deve perguntar se algum
assento vai ser reservado (caso existam ainda assentos disponíveis).
o Nenhuma passagem pode ser comercializada para ônibus que já partiram
(consultar o relógio do sistema).
 Permitir a geração dos relatórios (na tela ou em arquivo texto, escolha do usuário):
o Total arrecadado com venda de passagens no mês corrente para cada linha.
o Ocupação percentual média de cada linha em cada dia da semana (uma matriz).
 Além de receber as reservas pelo teclado, permitir ler as reservas de um arquivo texto
no seguinte formato:
o CIDADE, HORÁRIO(hh:mm), DATA(dd/mm/aaaa), ASSENTO
o Uma reserva por linha.
 Gravar em um arquivo texto todas as reservas que não puderam ser realizadas,
juntamente com o motivo (ex.: ônibus cheio, ônibus já partiu, assento ocupado).'''

"""Cidades de origem : Divinópolis, Claudio, Cajuru, São Roque de Minas, Belo Horizonte, Lagoa da Prata, Patrocínio
	Divinopolis -- Cajuru 				= 25 min 
	Divinópolis -- Claudio 				= 1 hora
	Divinópolis -- São Roque de Minas 	= 3 horas e 20
	Divinópolis -- Belo Horizonte 		= 2 horas e 30
	Divinópolis -- Lagoa da Prata 		= 1 hora e 40
	Divinópolis -- Patrocínio 	  		= 5 horas e 40
	
	Belo Horizonte -- São Roque de Minas 	= 6 horas e 40
	Belo Horizonte -- Carmo do Cajuru 	 	= 2 horas e 10 
	
"""
#=================================================	 BIBLIOTECAS	 =======================================================================
from colorama import Back, Fore, Style, init
#=================================================	MENSAGENS PADRÕES ===================================================================
erro_nao_inteiro = (Fore.RED+"||	  Apenas Numeros inteiros sao permitidos"+Style.RESET_ALL)
opcao_invalida = (Fore.RED+"||	Opção invalida!! Escolha novamente."+Style.RESET_ALL)
#=================================================	Variaveis Globais ===================================================================
onibus = 0
passagem = 0 
cidade_partida= 0
cidade_destino = 0
sair=0


#=================================================	Variaveis Globais =======================================================================

passagem=dict(zip(['Cidade de origem','Destino','Horário','Valor'],['Divinópolis',0,0,0]))
onibus=dict(zip(['Número','Assentos disponíveis','Data da partida (dia/mês/ano)'],[0,0,0]))
padrao_saida = list({"Divinópolis", "Belo Horizonte", "Lagoa da Prata", "Carmo do Cajuru"})
padrao_chegada =list({"Patrocínio", "Lagoa da Prata", "Carmo do Cajuru", "Belo Horizonte", "Divinopolis" } )

Linha_onibus_padrao = [
	{"Cidade de Saída" : padrao_saida[0], "Cidade de Chegada": padrao_chegada[0],"Horario Partida": "00:00", "Tempo de Viagem":"00:00", "Valor da Passagem":40.00}, #Divinopolis -- Patrocinio 
	{"Cidade de Saída" : padrao_saida[0], "Cidade de Chegada": padrao_chegada[1],"Horario Partida": "00:00", "Tempo de Viagem":"00:00", "Valor da Passagem":40.00}, #Divinipolis -- Lagoa da Prata
	{"Cidade de Saída" : padrao_saida[0], "Cidade de Chegada": padrao_chegada[2],"Horario Partida": "00:00", "Tempo de Viagem":"00:00", "Valor da Passagem":40.00}, #Divinopolis -- Carmo do Cajuru
	{"Cidade de Saída" : padrao_saida[0], "Cidade de Chegada": padrao_chegada[3],"Horario Partida": "00:00", "Tempo de Viagem":"00:00", "Valor da Passagem":40.00}, #Divinopolis -- Belo Horizonte

]
def Cadastrar_passagem():
	while True:
		print('-'*65)
		try:
			menu_passagem=int(input('Oque você deseja?\n||  1 - Inserir nova passagem\n||	2 - Excluir passagem\n||  3 - Alterar passagem:\n||	0 - Voltar ao Menu Principal\n'))
			match menu_passagem:
				case 1:
					adicionar_nova_passagem()
				case 2:
					excluir_passagem()
				case 3:
					alterar_passagem()
				case 0:
					print('Volte sempre!')
					return False
				case _:
					print(opcao_invalida)
		except ValueError:
			print(erro_nao_inteiro)

def adicionar_nova_passagem():
	print("Adicionando...")

def excluir_passagem():
	print("Excluindo...")

def alterar_passagem():
	print("Alterando...")

def Consultar_passagem():
	cidade_partida_usuario = input("|| Digite a cidade de Saída :")
	cidade_destino_usuario = input("|| Digite a cidade de Destino : ")
	onibus = int(input("|| Digite o numero do Ônibus: "))
	
def Consultar_assentos():
	print("Assentos disponiveis : 2")



print("="*75)
print(" 	SISTEMA DE UMA EMPRESA DE TRANSPORTE DE PASSAGEIROS.")
print(padrao_chegada[1])
print(padrao_saida[0])
print(Linha_onibus_padrao)
while True:
	print("-"*65)
	try:
		opcao_menu = int(input("||	1 - Exibir Tabela de Horários \n||	2 - Cadastrar nova passagem\n||	3 - Consultar passagens para determinada cidade\n||	4 - Consultar assentos disponíveis\n||	5-\n||	0 - Sair\n"))
		match opcao_menu:
			case 1:
				print("Exibindo Tabela...")
			case 2:
				print("Cadastrando nova passagem")
				Cadastrar_passagem()
				
			case 3:
				Consultar_passagem()

			case 4:
				Consultar_assentos()

			case 0:
				print("Finalizando sistema...")
				quit()
				
			case _: 
				print(opcao_invalida)
	except ValueError:
		print(erro_nao_inteiro)