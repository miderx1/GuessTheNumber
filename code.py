# -*- coding: utf-8 -*-
import random	# Biblioteca com função para gerar numero aleatório.
import numpy as np	# Biblioteca com função para gerar numero aleatório.
import os	# Biblioteca com função para limpar a tela.
import site

def jogar(d): 
	global win	# Puxando as variáveis globais para uso dentro da função.
	global loss	# Puxando as variáveis globais para uso dentro da função.
	
	if d == 1:	# Verifica a dificuldade escolhida.
		resp = np.random.randint(1,50)	# Sorteia um numero aleatório entre 1 e 50 e introduz na variável resp.
		lim = 50	# Define 50 como valor da variável 'lim', que será usada pra definir o limite máximo do numero sorteado em alguns comandos e strings.

	elif d == 2:
		resp = np.random.randint(1,100)
		lim = 100

	else:
		resp = np.random.randint(1,150)
		lim = 150

	tent = 10	# Define 10 tentativas para o usuário.

	while tent >= 1:	# Verifica se o usuário possui tentativas.
		os.system('CLS')	# Limpa a tela.

		print("Tentativas restantes: ",tent)		
		print("Digite um numero inteiro entre 1 e", str(lim))
		palp = int(input("Palpite: "))	# Recolhe o palpite do usuário.

		if palp >= 1 and palp <= lim:	# Verifica se o palpite dado pelo usuário está entre o intervalo proposto.
			if palp == resp:	# Verificar se o palpite está certo.
				os.system('CLS')

				win += 1	# Contabiliza uma vitória para o usuário.

				print("Parabéns, você acertou!")
				input()	# Input vazio para dar tempo do usuário ler a mensagem acima.
				break	# Cancela todos os comandos abaixos que estão inclusos dentro o While.
			else:	 
				os.system('CLS')

				if palp < resp:	# Verifica se o palpite é maior ou menor que a resposta sorteada.
					print("O numero", str(palp),"é menor que o numero sorteado") # Dá uma dica
					input()
				else:
					print("O numero", str(palp),"é maior que o numero sorteado") # Dá uma dica
					input()


		elif palp == 2020101367:	# Código que eu botei para testes.
			tent += 11 # Aumenta as tentativas em mais 10.
			os.system('CLS')
			print ("Trapaça Ativada! Você recebeu 10 tentativas.")
			input()

		elif palp == 40028922:	# Código que eu botei para testes.
			tent = 1 # Elimina todas as tentativas.
			os.system('CLS')
			print ("Trapaça Ativada! Você perdeu todas as tentativas.")
			input()
		else:	# Verifica a possibilidade do usuário ter posto um numero fora do limite estabelecido.
			os.system('CLS')

			print("Número fora do limite estabelecido.")
			input()
			tent += 1 # Aumenta as tentativas em 1 para que o usuário repita o ultimo palpite.

		tent -= 1 # Diminui as tentativas em um, já que o usuário acabou de usar uma.

	if tent == 0:	# Verifica se as tentativas acabaram.
		os.system('CLS')
		print("Tentativas finalizadas. Você perdeu.")
		print("O numero sorteado foi: ",str(resp)) # Mostra a resposta correta para o usuário.
		input()
		loss +=1


def login(): # Função para o login e cadastro
	global password # Globaliza a variável password para poder ser usada depois para fazer o backup.

	senha = "0"	# Define a variável para a a senha.
	menu = 0	# Define uma variável para o menu.

	while menu != 3:	# Faz a repetição do menu enquanto a opção selecionada não seja [3] Sair.
			os.system('CLS')
			print("\n Escolha uma das opções abaixo")
			print("[1] Logar")
			print("[2] Cadastrar")
			print("[3] Sair")

			menu = int(input("Opção: "))	# Coloca a opção escolhida pelo usuário na variável menu.

			if menu == 1:	# Verifica se a opção escolhida foi [1] Logar.
				os.system('CLS')
				log = input("Digite o login: ")	# Coloca o login digitado na variável log.

				try:	# Tenta abrir um arquivo com o login digitado acima, para verificar se o usuário existe.
					log_arq = open(log + ".txt","r")  # Abre o arquivo com os dados da conta do usuário.

				except: # Caso o usuário não exista, os codigos dentro do bloco abaixo serão executados.
					os.system('CLS')
					print("Login não encontrado") 
					input()
					continue # Vai cancelar todos os comandos dentro do bloco desse if.

				dados = log_arq.readline() # Coloca os dados do arquivo do usario na variável dados.
				dados = dados[0:(len(dados)-1)]     # Coleta a senha da conta encontrada, na variável dados, substituindo os dados anteriores.
				
				os.system('CLS')
				senha = input("Digite a senha: ") # Armazena a senha digitada pelo usuário na variável senha.

				if senha == dados:	# Verifica se a senha digitada é igual a senha da conta encontrada no arquivo.
					os.system('CLS')
					print("Logado com sucesso!") 
					input()
					menu = 3 # Variável menu recebe valor 3 para tirar do loop do while.

				else: # Conclue que a senha está incorreta
					os.system('CLS') 
					print("Senha incorreta!")
					input()

				log_arq.close() # Fecha o arquivo aberto. Pois o login ja foi feito, ou cancelado.

			elif menu > 3 or menu < 1: # Verifica se a opção escolhida é maior que 3 ou menor que 1, ou seja, inválida.
				os.system('CLS')
				print("Opção Inválida!")
				input()	

			elif menu == 2: # Verifica se a opção escolhida foi [2] Cadastrar.
				os.system('CLS')

				log = input("Digite o login: ") # Armazena o login digitado na variável log

				try: # Tenta abrir um arquivo com o login digitado acima, para verificar se o usuário já existe.
					log_arq = open(log + ".txt","r") 
					print("Login já registrado!")
					input()
					continue # Pula todos os comandos dentro desse elif e abaixo dessa linha.

				except: # Conclue que o usuário não existente está apto a ser criado.
					log_arq = open(log + ".txt","w+") # Cria um arquivo para armazenar os dados da nova conta.


				dados = log_arq.readlines() # Armazena os dados do arquivo na variável dados.

				os.system('CLS')

				senha = input("Digite uma senha: ") # Armazena a senha digitada pelo usuário na variável senha

				log_arq.write(senha) # Armazena a senha no arquivo da conta.
				log_arq.write("\n")  # Pula uma linha dentro do arquivo de texto.
				log_arq.close()		# Fecha o arquivo

				os.system('CLS')
				print("Registrado com sucesso!")
				menu = 3 # Coloca o valor 3 na variável menu para interromper a repetição.
				input()
			else:
				quit() # Fecha o programa caso a opção escolhida for [4] Sair.

	password = senha # A variável global password recebe o valor da variável senha, que foi digitado pelo usuário.
	
	return log # Retorna o nome de usuário.

log = login() # Variável global log recebe o valor retornado na função login().

def testarquivo(): # Função para testar se o arquivo da conta existe.
	global log # Puxa a variável global para uso dentro da função.

	try:	# Testa a abertura do arquivo da conta.
		perfil = open(log+ ".txt","r")
		arq = 0 # Caso o arquivo seja aberto com sucesso, a variável arq recebe o valor 0.

	except:
		arq = 1 # Caso o arquivo não possa ser aberto, ou não exista, a variável arq recebe valor 1.

	return arq # Retorna o valor de arq.



win = 0		# Define a variável win para contabilizar as vitórias.
loss = 0	# Define a variável loss para contabilizar as Derrotas.
menu = 0	# Define a variável menu para uso no menu de escolhas.
perf = testarquivo() # Define a variavel perf e armazena o valor retornado na função testarquivo().

if perf == 0: # Verifica se não é a primeira vez que o perfil é aberto, para recuperar o backup.
	backup = open(log + ".txt","r") # Abre o arquivo da conta, em modo leitura, e passa os dados para a variável backup.
	winrate = backup.readlines() # Pega a taxa de vitória armazenada no backup e armazena na variável winrate.

	# O bloco de comando abaixo é pra garantir que os dados de vitória e de derrota do backup 
	# sejam puxadas corretamente. Pois algumas contas que eu criei para testar acabaram pulando uma linha
	# entre as linhas de vitória e derrota.

	if len(winrate) > 1: 
		if len(winrate) > 3:
			win = int(winrate[1])
			loss = int(winrate[3])
		else:
			win = int(winrate[1])
			loss = int(winrate[2])


	backup.close() # Fecha o arquivo de backup, pois o mesmo ja foi feito.


while menu != 3: 

	if win+loss != 0: 					# Verifica se a soma das vitórias e derrotas são maiores que 0.
		wr = (win / (win+loss))*100		# Caso seja maior que 0, o calculo é feito e a porcentagem de vitória é armazenada na variável wr.
	else: 
		wr = 0 # Caso a soma seja igual a 0, a variável wr recebe o valor 0.

	os.system('CLS')
	print("Usuário: "+ log +"\n")
	print("Vitórias: ",win)
	print("Derrotas: ",loss)
	print("Winrate: ",round(wr),"%")
	print("\n Escolha uma das opções abaixo")
	print("[1] Jogar")
	print("[2] Limpar Winrate")
	print("[3] Sair")
	
	menu = int(input(": ")) # Armazena a opção escolhida na variável menu.
	
	if menu == 1:

		menu2 = 5 # Define a variável menu2, com um numero maior que 4 para a repetição poder começar.

		while menu2 > 4: 
			os.system('CLS')
			print("Usuário: "+ log +"\n")
			print("Vitórias: ",win)
			print("Derrotas: ",loss)
			print("Winrate: ",round(wr),"%")
			print("\n Escolha uma das dificuldades abaixo")
			print("[1] Fácil    (De 1 a 50)")
			print("[2] Médio    (De 1 a 100) ")
			print("[3] Difícil  (De 1 a 150)")
			print("[4] Sair")
			menu2 = int(input(": "))
			if menu2 == 1:
				jogar(1)	# Caso a opção escolhida seja [1] Facil, o jogo começará nesta dificuldade
			elif menu2 == 2:
				jogar(2)	# Caso a opção escolhida seja [2] Médio, o jogo começará nesta dificuldade
			elif menu2 == 3:
				jogar(3)	# Caso a opção escolhida seja [3] Difícil, o jogo começará nesta dificuldade
			elif menu2 == 4:
				continue	# Caso a opçao escolhida seja [4] Sair, a repetição será interrompida.
			else:	
				print("Opção Inválida!")
				input()

	elif menu > 3 or menu < 1:	# Opção inválida
		os.system('CLS')
		print("Opção Inválida!")
		input()

	elif menu == 2: # Opção para resentar as vitórias e derrotas
		win = 0
		loss = 0
		os.system('CLS')
		print("Winrate apagado!")
		input()

	else:	# Opção para salvar o backup e fechar o programa.
		backup = open(log + ".txt","w") #Regrava informação
		backup.write(password)
		backup.write("\n")
		backup.write(str(win))
		backup.write("\n")
		backup.write(str(loss))
		backup.close()

	
os.system('CLS')

print("Jogo Encerrado, e Backup salvo")




