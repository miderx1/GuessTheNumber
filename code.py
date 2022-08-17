# -*- coding: utf-8 -*-
import random 
import numpy as np 
import os
import site

def jogar(d):
	global win #
	global loss
	
	if d == 1:
		resp = np.random.randint(1,50)
		lim = 50

	elif d == 2:
		resp = np.random.randint(1,100)
		lim = 100

	else:
		resp = np.random.randint(1,150)
		lim = 150

	tent = 10

	while tent >= 1:
		os.system('CLS')

		print("Tentativas restantes: ",tent)
		print("Digite um numero inteiro entre 1 e", str(lim))
		palp = int(input("Palpite: "))

		if palp >= 1 and palp <= lim:
			if palp == resp:
				os.system('CLS')

				win += 1

				print("Parabéns, você acertou!")
				input()
				break
			else:
				os.system('CLS')

				if palp < resp:
					print("O numero", str(palp),"é menor que o numero sorteado")
					input()
				else:
					print("O numero", str(palp),"é maior que o numero sorteado")
					input()


		elif palp == 2020101367:
			tent += 11
			os.system('CLS')
			print ("Trapaça Ativada! Você recebeu 10 tentativas.")
			input()

		elif palp == 40028922:
			tent = 1
			os.system('CLS')
			print ("Trapaça Ativada! Você perdeu todas as tentativas.")
			input()
		else:
			os.system('CLS')

			print("Número fora do limite estabelecido.")
			input()
			tent += 1

		tent -= 1

	if tent == 0:
		os.system('CLS')
		print("Tentativas finalizadas. Você perdeu.")
		print("O numero sorteado foi: ",str(resp))
		input()
		loss +=1


def login():
	global password

	senha = "0"
	menu = 0

	while menu != 3:
			os.system('CLS')
			print("\n Escolha uma das opções abaixo")
			print("[1] Logar")
			print("[2] Registrar")
			print("[3] Sair")

			menu = int(input("Opção: "))

			if menu == 1:
				os.system('CLS')
				log = input("Digite o login: ")

				try:
					log_arq = open(log + ".txt","r")

				except:
					os.system('CLS')
					print("Login não encontrado")
					input()
					continue

				dados = log_arq.readline()
				dados = dados[0:(len(dados)-1)]
				
				os.system('CLS')
				senha = input("Digite a senha: ")

				if senha == dados:
					os.system('CLS')
					print("Logado com sucesso!")
					input()

					menu = 3

					continue

				else:
					os.system('CLS')
					print("Senha incorreta!")
					input()

				log_arq.close()

			elif menu > 3 or menu < 1:
				os.system('CLS')
				print("Opção Inválida!")
				input()#Opção errada

			elif menu == 2: #Registrar
				os.system('CLS')

				log = input("Digite o login: ")

				try:
					log_arq = open(log + ".txt","r")
					print("Login já registrado!")
					input()
					continue
				except:
					log_arq = open(log + ".txt","w+")


				dados = log_arq.readlines()

				os.system('CLS')

				senha = input("Digite uma senha: ")

				log_arq.write(senha)
				log_arq.write("\n")
				log_arq.close()

				os.system('CLS')
				print("Registrado com sucesso!")
				menu = 3
				input()
			else:
				quit()

	password = senha
	return log

log = login()

def testarquivo(): 
	global log

	try:
		perfil = open(log+ ".txt","r")
		arq = 0

	except:
		arq = 1

	return arq



win = 0
loss = 0
menu = 0
perf = testarquivo()



if perf == 0:
	backup = open(log + ".txt","r") #Modo leitura
	winrate = backup.readlines()

	if len(winrate) > 1:
		if len(winrate) > 3:
			win = int(winrate[1])
			loss = int(winrate[3])
		else:
			win = int(winrate[1])
			loss = int(winrate[2])


	backup.close()


while menu != 3:

	if win+loss != 0:
		wr = (win / (win+loss))*100
	else: 
		wr = 0

	os.system('CLS')
	print("Usuário: "+ log +"\n")
	print("Vitórias: ",win)
	print("Derrotas: ",loss)
	print("Winrate: ",round(wr),"%")
	print("\n Escolha uma das opções abaixo")
	print("[1] Jogar")
	print("[2] Limpar Winrate")
	print("[3] Sair")
	
	menu = int(input(": "))
	
	if menu == 1:

		menu2 = 5

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
				jogar(1)
			elif menu2 == 2:
				jogar(2)
			elif menu2 == 3:
				jogar(3)
			elif menu2 == 4:
				continue
			else:
				print("Opção Inválida!")
				input()

	elif menu > 3 or menu < 1:
		os.system('CLS')
		print("Opção Inválida!")
		input()

	elif menu == 2:
		win = 0
		loss = 0
		os.system('CLS')
		print("Winrate apagado!")
		input()

	else:
		backup = open(log + ".txt","w") #Regrava informação
		backup.write(password)
		backup.write("\n")
		backup.write(str(win))
		backup.write("\n")
		backup.write(str(loss))
		backup.close()

	
os.system('CLS')

print("Jogo Encerrado, e Backup salvo")




